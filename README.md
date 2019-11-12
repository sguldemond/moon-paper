### Requirements

Geckodriver:
```
sudo apt install firefox-geckodriver
```

### Sources

http://neoprogrammics.com/ > Lunar Phase Image Sets > near_side_1024x1024X8.7z

https://commons.wikimedia.org/wiki/User:JayTanner/lunar-west-side-phase-set

https://www.timeanddate.com/moon/phases/netherlands/amsterdam


### Phase Orientation Legend

ANGLE    PHASE             EYE VIEW
000      New Moon          Sun horizontally aligned with Moon
090      First Quarter     Sun directly to right
180      Full Moon         Sun directly behind
270      Last Quarter      Sun directly to left
360      New Moon          Sun horizontally aligned with Moon

Between phases there are 90 images available
I have to spread out these 90 images over the times in between every moon phase, e.g.:

New Moon = 6 Jan 2019 02:28
First Quarter = 14 Jan 2019 07:45

Difference in minutes is:

-   8 days = 11520 minutes
-   02:28 > 07:45 = 
    32 min +
    4 hour = 240 min +
    45 min = 317 minutes

11520 + 317 = 11837 minutes

11837 / 90 = 131,52 = 132 minutes per image
max update rate is every 2 hours and 12 minutes

10 updates per day, every 144 minutes

6 januari
00:00 > 02:24: image # 359
02:25 > 04:49: image # 000

# TODO:
save schedule per day with every image for every 144 minutes

print out every 144 minutes

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
