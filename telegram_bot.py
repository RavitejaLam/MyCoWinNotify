import logging

import requests


def send_message(msg_list, chat_id, bot_token):
    for msg in msg_list:
        send_api = 'https://api.telegram.org/bot' + bot_token + \
                   '/sendMessage?chat_id=' + chat_id + \
                   '&parse_mode=MarkdownV2&text=' + msg.replace('-', ':')
        response = requests.get(send_api)
        if response.status_code != 200:
            logging.error("Failed to Send Notification")
            exit(1)
    logging.info("Notification Sent")
