#!/usr/bin/env python3
"""
AI Trade Bot - Core Orchestrator

Main controller for the AI-powered Forex trading bot.
Handles initialization, coordination of modules, and main trading loop.

Author: ssrajesh20-alcemax
Version: 1.0.0
Date: 2025-09-27
"""

import asyncio
import logging
import signal
import sys
from datetime import datetime
from pathlib import Path

# Add project root to path for imports
sys.path.append(str(Path(__file__).parent.parent))

from core.config import ConfigManager
from core.logger import setup_logging
from integration.telegram_bot import TelegramBot
from integration.oanda_api import OandaAPI
from utils.risk_management import RiskManager


class BotOrchestrator:
    """
    Main orchestrator class that coordinates all bot components
    """
    
    def __init__(self):
        self.config = None
        self.logger = None
        self.telegram_bot = None
        self.oanda_api = None
        self.risk_manager = None
        self.is_running = False
        self.shutdown_event = asyncio.Event()
        
    async def initialize(self):
        """
        Initialize all bot components
        """
        try:
            # Load configuration
            self.config = ConfigManager()
            await self.config.load_config()
            
            # Setup logging
            self.logger = setup_logging(self.config.get('logging', {}))
            self.logger.info("AI Trade Bot starting up...")
            
            # Initialize components
            await self._initialize_components()
            
            self.logger.info("Bot initialization completed successfully")
            return True
            
        except Exception as e:
            if self.logger:
                self.logger.error(f"Failed to initialize bot: {str(e)}")
            else:
                print(f"Critical error during initialization: {str(e)}")
            return False
    
    async def _initialize_components(self):
        """
        Initialize individual bot components
        """
        # Initialize OANDA API
        oanda_config = self.config.get('oanda', {})
        if oanda_config.get('enabled', True):
            self.oanda_api = OandaAPI(oanda_config)
            await self.oanda_api.initialize()
            self.logger.info("OANDA API initialized")
        
        # Initialize Telegram bot
        telegram_config = self.config.get('telegram', {})
        if telegram_config.get('enabled', False):
            self.telegram_bot = TelegramBot(telegram_config)
            await self.telegram_bot.initialize()
            self.logger.info("Telegram bot initialized")
        
        # Initialize risk manager
        risk_config = self.config.get('risk_management', {})
        self.risk_manager = RiskManager(risk_config)
        self.logger.info("Risk manager initialized")
    
    async def start(self):
        """
        Start the main trading loop
        """
        self.is_running = True
        self.logger.info("Starting main trading loop")
        
        if self.telegram_bot:
            await self.telegram_bot.send_message("🚀 AI Trade Bot started successfully!")
        
        try:
            while self.is_running and not self.shutdown_event.is_set():
                await self._trading_cycle()
                await asyncio.sleep(1)  # 1-second cycle
                
        except Exception as e:
            self.logger.error(f"Error in main trading loop: {str(e)}")
            if self.telegram_bot:
                await self.telegram_bot.send_message(f"❌ Trading loop error: {str(e)}")
        
        finally:
            await self.shutdown()
    
    async def _trading_cycle(self):
        """
        Execute one cycle of the trading logic
        """
        try:
            # Get current market data
            if self.oanda_api:
                # This is a placeholder for actual trading logic
                # In a real implementation, this would:
                # 1. Fetch current market data
                # 2. Run analysis and strategies
                # 3. Check risk management rules
                # 4. Execute trades if conditions are met
                pass
                
        except Exception as e:
            self.logger.error(f"Error in trading cycle: {str(e)}")
    
    async def shutdown(self):
        """
        Gracefully shutdown the bot
        """
        self.logger.info("Shutting down AI Trade Bot...")
        self.is_running = False
        
        if self.telegram_bot:
            await self.telegram_bot.send_message("🛑 AI Trade Bot shutting down...")
            await self.telegram_bot.shutdown()
        
        if self.oanda_api:
            await self.oanda_api.shutdown()
        
        self.logger.info("AI Trade Bot shutdown completed")
    
    def signal_handler(self, signum, frame):
        """
        Handle shutdown signals
        """
        self.logger.info(f"Received signal {signum}, initiating shutdown...")
        self.shutdown_event.set()


async def main():
    """
    Main entry point
    """
    bot = BotOrchestrator()
    
    # Setup signal handlers
    signal.signal(signal.SIGINT, bot.signal_handler)
    signal.signal(signal.SIGTERM, bot.signal_handler)
    
    # Initialize and start bot
    if await bot.initialize():
        try:
            await bot.start()
        except KeyboardInterrupt:
            print("\nKeyboard interrupt received")
        except Exception as e:
            print(f"Unexpected error: {str(e)}")
    else:
        print("Failed to initialize bot")
        sys.exit(1)


if __name__ == "__main__":
    print("AI Trade Bot v1.0.0")
    print("Starting up...")
    
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nBot stopped by user")
    except Exception as e:
        print(f"Fatal error: {str(e)}")
        sys.exit(1)
