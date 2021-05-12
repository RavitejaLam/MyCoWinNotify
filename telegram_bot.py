import logging

import requests


def send_message(msg, chat_id, bot_token):
    send_api = 'https://api.telegram.org/bot' + bot_token + \
               '/sendMessage?chat_id=' + chat_id + \
               '&parse_mode=MarkdownV2&text=' + msg
    response = requests.get(send_api)
    if response.status_code == 200:
        logging.error("Notification Sent")
    else:
        logging.error("Failed to Send Notification")
