import logging
import random

import requests as req
from bs4 import BeautifulSoup


def get_random_user_agent(browser):
    url = 'http://www.useragentstring.com/pages/useragentstring.php?name=' + browser
    r = req.get(url)

    if r.status_code == 200:
        soup = BeautifulSoup(r.content, 'html.parser')
    else:
        soup = False

    if soup:
        div = soup.find('div', {'id': 'liste'})
        lnk = div.findAll('a')

        random_index = random.randint(0, len(lnk) - 1)

        logging.debug(lnk[random_index].text)
        return lnk[random_index].text
    else:
        logging.error("Failed to get user agent")
        exit(1)
