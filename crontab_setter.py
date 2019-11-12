from crontab import CronTab
from datetime import datetime, timedelta

import os

dbus_var = os.environ.get('DBUS_SESSION_BUS_ADDRESS')

cron = CronTab(user='stan')
cron.env['DBUS_SESSION_BUS_ADDRESS'] = dbus_var

job = cron.new(command='/home/stan/Projects/Other/moon-phases/change_background.py')
job.hour.every(2)

# now = datetime.now()
# then = now + timedelta(minutes=1)
# job.setall(then)

cron.write()