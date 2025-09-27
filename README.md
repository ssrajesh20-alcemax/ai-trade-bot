# AI Trade Bot

## Overview
AI-powered Forex trading bot with multi-timeframe analysis, Telegram integration, news sentiment analysis, and automated execution capabilities. This project combines the best practices from modern AI Forex bots with cutting-edge features for professional algorithmic trading.

## Features

### Core AI Trading Capabilities
- **Multi-timeframe Analysis**: Analyzes price patterns across multiple timeframes (M1, M5, M15, H1, H4, D1)
- **Machine Learning Models**: Implements TensorFlow/PyTorch models for price prediction
- **Technical Indicator Integration**: RSI, MACD, Bollinger Bands, Moving Averages, and custom indicators
- **Risk Management**: Dynamic stop-loss, take-profit, and position sizing algorithms
- **Backtesting Engine**: Historical data analysis and strategy optimization

### Advanced Features
- **News Sentiment Analysis**: Real-time news scraping and sentiment scoring affecting currency pairs
- **Telegram Integration**: Live trade notifications, manual control, and performance reports
- **TradingView Compatibility**: Webhook support for TradingView alerts and strategy execution
- **n8n Workflow Integration**: Automated workflows for data processing and trade execution
- **Economic Calendar Integration**: Automatic adjustment during high-impact news events

### Broker Support
- **OANDA API**: Direct integration with OANDA's REST API and streaming prices
- **MetaTrader Support**: MQL4/MQL5 bridge for MetaTrader platforms
- **Paper Trading**: Safe testing environment with simulated trades

### Monitoring & Control
- **Real-time Dashboard**: Web-based interface for monitoring active positions
- **Performance Analytics**: Detailed P&L tracking, win rate, and risk metrics
- **Alert System**: Email, SMS, and Telegram notifications for critical events
- **Remote Management**: Mobile app compatibility for on-the-go monitoring

## Project Structure

```
ai-trade-bot/
├── core/                    # Core bot orchestration
│   ├── bot_orchestrator.py  # Main bot controller
│   ├── config.py           # Configuration management
│   └── logger.py           # Logging utilities
├── strategies/              # Trading strategies (Future development)
│   ├── __init__.py
│   ├── base_strategy.py
│   └── ml_strategies/
├── integration/             # External service integrations
│   ├── telegram_bot.py     # Telegram notifications and control
│   ├── oanda_api.py        # OANDA broker integration
│   └── tradingview_webhook.py # TradingView webhook handler
├── backtest/               # Backtesting framework (Future development)
│   ├── __init__.py
│   ├── backtest_engine.py
│   └── data_manager.py
├── utils/                  # Utility functions
│   ├── __init__.py
│   ├── indicators.py
│   └── risk_management.py
├── data/                   # Data storage
│   ├── models/            # ML models
│   ├── historical/        # Historical price data
│   └── config/           # Configuration files
├── tests/                 # Unit tests
├── docs/                  # Documentation
├── requirements.txt       # Python dependencies
├── config.yaml           # Main configuration
├── docker-compose.yml    # Docker setup
└── README.md             # This file
```

## Quick Start

### Prerequisites
- Python 3.8+
- OANDA trading account (demo or live)
- Telegram bot token (optional)
- TradingView account (optional)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/ssrajesh20-alcemax/ai-trade-bot.git
cd ai-trade-bot
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure settings:
```bash
cp config.yaml.example config.yaml
# Edit config.yaml with your API keys and preferences
```

4. Run the bot:
```bash
python core/bot_orchestrator.py
```

## Configuration

### API Keys Required
- **OANDA API**: Account ID and access token
- **Telegram Bot**: Bot token from @BotFather
- **News API**: For sentiment analysis (NewsAPI, Alpha Vantage)
- **TradingView**: Webhook URLs (optional)

### Risk Management Settings
- Maximum risk per trade: 1-2% of account balance
- Maximum concurrent positions: 3-5 pairs
- Daily loss limit: 5% of account balance
- Drawdown protection: Stop all trading at 10% account drawdown

## Trading Strategies (Planned)

1. **Trend Following**: Multi-timeframe trend analysis with AI confirmation
2. **Mean Reversion**: Statistical arbitrage on currency pairs
3. **News Trading**: Sentiment-based trading around economic events
4. **Scalping**: High-frequency micro-movements with ML prediction
5. **Carry Trading**: Interest rate differential strategies

## Development Roadmap

### Phase 1 (Current) - Foundation
- [x] Project structure setup
- [x] Basic configuration system
- [x] OANDA API integration
- [x] Telegram bot integration
- [ ] Core orchestrator implementation

### Phase 2 - Core Features
- [ ] Multi-timeframe data collection
- [ ] Basic trading strategies
- [ ] Risk management system
- [ ] Backtesting framework

### Phase 3 - AI Enhancement
- [ ] Machine learning models
- [ ] News sentiment analysis
- [ ] Advanced strategy optimization
- [ ] Performance analytics dashboard

### Phase 4 - Production Ready
- [ ] Full test coverage
- [ ] Docker deployment
- [ ] Cloud hosting setup
- [ ] Mobile app interface

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Disclaimer

⚠️ **Risk Warning**: Trading foreign exchange and CFDs carries a high level of risk and may not be suitable for all investors. Past performance does not guarantee future results. This software is for educational and research purposes. Use at your own risk.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

- **Author**: ssrajesh20-alcemax
- **Project Link**: https://github.com/ssrajesh20-alcemax/ai-trade-bot
- **Issues**: https://github.com/ssrajesh20-alcemax/ai-trade-bot/issues

## Acknowledgments

- OANDA API for reliable forex data and execution
- TradingView for charting and analysis tools
- Telegram for real-time notifications
- The open-source trading community for inspiration and libraries

---

**Note**: This is an active development project. Features marked as "Future development" are planned but not yet implemented. The initial release focuses on core infrastructure and basic trading capabilities.
