# BTC Notifications via Telegram bot

## What is this?

This is a simple python script designed to send a message through Telegram detailing the last n number of BTC prices
- The message Interval can be adjusted
- The number of historical prices can be adjusted

## Requirements

BTC Notifications was written in Python 3.9.1 and uses the following modules
- requests
- time

You will also need:
- a CoinMarketCap API key
- a Telegram chat bot
- your personal Telegram chat ID

## Inspiration
This small script is strongly based on the following two sources as I made it in the context of basis Python training
- https://itnext.io/lets-build-a-real-time-bitcoin-price-notification-project-using-python-daaa7391f71b
- https://realpython.com/python-bitcoin-ifttt/

Minor adjustments include:
- External config file that contains sensitive information like API keys
- Moved the first url declaration to decrease line length (pep8)
- Split second URL to two lines for the same reason
