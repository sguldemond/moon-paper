## Moon Paper

Update your wallpaper with the an image of the current phase of the moon.

*Work in progress:*
Want to work towards being able to just define your location, e.g. 'netherlands/amsterdam',
and get the current moon phase based on your location as live wallpaper.

### Requirements

Geckodriver (for scraping 'timeanddate.com/moon/phases'):
```
sudo apt install firefox-geckodriver
```

Download pictures of the moon at:

http://neoprogrammics.com/ > Lunar Phase Image Sets > near_side_1024x1024X8.7z


### Sources

- https://commons.wikimedia.org/wiki/User:JayTanner/lunar-west-side-phase-set
- https://www.timeanddate.com/moon/phases/netherlands/amsterdam


### Phase Orientation Legend

ANGLE    PHASE             EYE VIEW
000      New Moon          Sun horizontally aligned with Moon
090      First Quarter     Sun directly to right
180      Full Moon         Sun directly behind
270      Last Quarter      Sun directly to left
360      New Moon          Sun horizontally aligned with Moon

### Notes

List all cron jobs (of current user):
```
crontab -l
```

Bash without profile:
```
env -i /bin/bash --noprofile --norc
```

Tunnel output to files
```
some_script.sh 1> /dev/null 2> /other/path/to/some_job.err
```

From `man dconf`: _"Note that dconf needs a D-Bus session bus connection to write changes to the dconf database."_
```
# echo $DBUS_SESSION_BUS_ADDRESS
# ./noprofile.sh
# dbus-launch
# export $(dbus-launch)
```
Source: https://stackoverflow.com/questions/41242460/how-to-export-dbus-session-bus-address
