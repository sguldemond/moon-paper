from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup

import json
from datetime import datetime

options = Options()
options.add_argument('--headless')
driver = webdriver.Firefox(options=options, executable_path='/usr/bin/geckodriver')

with open('./config.json', 'r') as config_file:
    config = config_file.read()

# location is set automatically based on location of user
url = 'https://www.timeanddate.com/moon/phases/'
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


def get_date(date, time):
    year = datetime.now().year
    
    if date == '\xa0':
        return None
    
    date_string = '{0} {1} {2}'.format(date, year, time)
    return datetime.strptime(date_string, '%d %b %Y %H:%M').strftime('%Y-%m-%d %H:%M')


def append_schedule(_type, _date, image_id):
    phase_schedule.append({
        'type': _type,
        'date_time': _date,
        'image_id': image_id
    })


for tr in trs:
    tds = tr.find_all('td')
    tds = tds[:8]

    date1 = get_date(tds[0].text, tds[1].text)
    if date1: append_schedule('New Moon', date1, '000')

    date2 = get_date(tds[2].text, tds[3].text)
    if date2: append_schedule('First Quarter', date2, '090')

    date3 = get_date(tds[4].text, tds[5].text)
    if date3: append_schedule('Full Moon', date3, '180')

    date4 = get_date(tds[6].text, tds[7].text)
    if date4: append_schedule('Third Quarter', date4, '270')
    

print(json.dumps(phase_schedule))