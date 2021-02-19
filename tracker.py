"""Monitor BTC prices and send a periodic message through Telegram."""
import requests
import time
from config import api_key, api_url, bot_token,\
 threshold, chat_id, time_interval


def get_btc_price():
    """Pull BTC price from coinmarketcap."""
    headers = {
        'Accept': 'application/json',
        'X-CMC_PRO_API_KEY': api_key
    }

    # make a request to the coinmarketcap api
    response = requests.get(api_url, headers=headers)
    response_json = response.json()
    # print(response_json)

    # extract the bitcoin price from the json data
    btc_price = response_json['data'][0]
    return btc_price['quote']['USD']['price']


# function to send message through telegram
def send_message(chat_id, msg):
    """Send messages through Telegram."""
    url = f"https://api.telegram.org/bot{bot_token}/\
    sendMessage?chat_id={chat_id}&text={msg}"

    # send the message
    requests.get(url)


# main function
def main():
    """Run main loop."""
    price_list = []

    # infinite loop
    while True:
        price = get_btc_price()
        price_list.append(price)

        # if the price falls below threshold, immediate message
        if price < threshold:
            send_message(chat_id=chat_id, msg=f'BTC Price Drop Alert: {price}')

        # send last 6 BTC prices
        if len(price_list) >= 6:
            send_message(chat_id=chat_id, msg=price_list)
            # empty price_list
            price_list = []

        # fetch price for every dash minutes
        time.sleep(time_interval)


# activate main
if __name__ == '__main__':
    main()
