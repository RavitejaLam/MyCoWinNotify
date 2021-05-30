#!/usr/bin/python3
import logging
from cowin import get_sessions
import datetime
import telegram_bot
import constant

if __name__ == '__main__':
    logging.basicConfig(filename='/home/ravitejalam/Desktop/cowin.log',
                        filemode='a',
                        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                        datefmt='%H:%M:%S',
                        level=logging.DEBUG)

    req_age = 25
    valid_sessions = []

    for i in range(5):
        date = (datetime.date.today() + datetime.timedelta(i)).strftime("%d-%m-%Y")
        valid_sessions.extend(get_sessions(date, req_age))

    if len(valid_sessions):
        for chat_id in constant.CHAT_IDS:
            telegram_bot.send_message(valid_sessions, str(chat_id), str(constant.BOT_TOKEN))
    else:
        logging.info("Currently no centers for age < " + str(req_age) + " in visakhapatnam")
