#!/usr/bin/python3
import json
import logging

import requests
import datetime
import telegram_bot
import constant
import ua

logging.basicConfig(filename='/home/ravitejalam/Desktop/cowin.log',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)


def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


def get_info(center, session):
    return "name: " + str(center['name']) + " address: " + str(center['address']) + " date: " + str(
        session['date']) + " vaccine: " + str(session['vaccine']) + " available: " + str(
        session['available_capacity']) + " age: " + str(session['min_age_limit'])


def get_sessions(date):
    logging.info("Running for date : " + date)
    # user_agent = ua.get_random_user_agent("Chrome")
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
    headers = {
        'User-Agent': user_agent,
        'From': 'ryuk@cowin.com'
    }
    cowin_api = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=8&date=" + date
    response = requests.get(cowin_api, headers=headers)

    if response.status_code != 200:
        logging.error("Failed to get CoWin API with status" + str(response.status_code))
        logging.debug("response json: " + response.json())
        exit(1)

    centers = response.json()['centers']
    for center in centers:
        for session in center['sessions']:
            if session['min_age_limit'] < req_age and int(session['available_capacity_dose1']) > 0:
                valid_sessions.append(get_info(center, session))


req_age = 25
valid_sessions = []

for i in range(30):
    date = (datetime.date.today() + datetime.timedelta(i)).strftime("%d-%m-%Y")
    get_sessions(date)

if len(valid_sessions):
    chat_ids = list(str(constant.CHAT_ID).strip('(').strip(')').split(','))
    for chat_id in chat_ids:
        telegram_bot.send_message(valid_sessions, str(chat_id), str(constant.BOT_TOKEN))
else:
    logging.info("Currently no centers for age < " + str(req_age) + " in visakhapatnam")
