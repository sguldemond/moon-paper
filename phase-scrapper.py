from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup

import json
from datetime import datetime

options = Options()
options.add_argument('--headless')
driver = webdriver.Firefox(firefox_options=options, executable_path='/usr/bin/geckodriver')

url = 'https://www.timeanddate.com/moon/phases/netherlands/amsterdam'
# url = 'file:///home/stan/Projects/Other/moon-phases/Moon%20Phases%202019%20%E2%80%93%20Lunar%20Calendar%20for%20Amsterdam,%20Netherlands.html'
driver.get(url)

el = driver.find_elements_by_css_selector('table.zebra')
table = el[0].get_attribute('innerHTML')

soup = BeautifulSoup(table, features="html.parser")

headers = [header.text for header in soup.find('thead').find_all('th')]
# New Moon > Third Quarter
headers = headers[1:5]
# print(headers)

trs = soup.find('tbody').find_all('tr')

phase_schedule = []

year = 2019

def get_date(date, time, year=2019):
    if date == '\xa0':
        return None
    
    date_string = '{0} {1} {2}'.format(date, year, time)
    return datetime.strptime(date_string, '%d %b %Y %H:%M').strftime('%Y-%m-%d %H:%M')

for tr in trs:
    tds = tr.find_all('td')
    tds = tds[:8]

    # full_cycle = []        

    phase_schedule.append({
        'type': 'New Moon',
        'date_time': get_date(tds[0].text, tds[1].text),
        'image_id': '000'
    })

    phase_schedule.append({
        'type': 'First Quarter',
        'date_time': get_date(tds[2].text, tds[3].text),
        'image_id': '090'
    })

    phase_schedule.append({
        'type': 'Full Moon',
        'date_time': get_date(tds[4].text, tds[5].text),
        'image_id': '180'
    })

    phase_schedule.append({
        'type': 'Third Quarter',
        'date_time': get_date(tds[6].text, tds[7].text),
        'image_id': '270'
    })

    # phase_schedule.append(full_cycle)


print(json.dumps(phase_schedule))