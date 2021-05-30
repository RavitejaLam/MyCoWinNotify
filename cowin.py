import requests
import json
import ua
import logging


def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


def get_info(center, session):
    return "name: " + str(center['name']) + " address: " + str(center['address']) + " date: " + str(
        session['date']) + " vaccine: " + str(session['vaccine']) + " available: " + str(
        session['available_capacity']) + " age: " + str(session['min_age_limit'])


def get_sessions(date, req_age):
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
    valid_sessions = []
    for center in centers:
        for session in center['sessions']:
            if session['min_age_limit'] < req_age and int(session['available_capacity_dose1']) > 0:
                valid_sessions.append(get_info(center, session))

    return valid_sessions
