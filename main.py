import json
import logging

import requests
import datetime
import telegram_bot
import constant
import ua


def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


def get_sessions(date):
    logging.info("Running for date : " + date)
    headers = {
        'User-Agent': ua.get_random_user_agent("Chrome"),
        'From': 'ryuk@cowin.com'
    }
    response = requests.get(
        "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=8&date=" + date,
        headers=headers)

    if response.status_code != 200:
        logging.error("Failed to get CoWin API")
        exit(1)

    centers = response.json()['centers']
    for center in centers:
        for session in center['sessions']:
            if session['min_age_limit'] < 25:
                valid_sessions.append(session)


valid_sessions = []

for i in range(30):
    date = (datetime.date.today() - datetime.timedelta(i)).strftime("%d-%m-%Y")
    get_sessions(date)

if len(valid_sessions):
    telegram_bot.send_message(str(valid_sessions), str(constant.CHAT_ID), str(constant.BOT_TOKEN))
