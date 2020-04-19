from crontab import CronTab
from datetime import datetime, timedelta

import os
import getpass

dbus_var = os.environ.get('DBUS_SESSION_BUS_ADDRESS')

user = getpass.getuser()

cron = CronTab(user=user)
cron.env['DBUS_SESSION_BUS_ADDRESS'] = dbus_var

job = cron.new(command="/home/{user}/moon-paper/change_background.py".format(user=user))
job.hour.every(2)

cron.write()