# Moon Paper

Update your wallpaper with the an image of the real time phase of the moon.

Currently working with Ubuntu running Gnome 3.34.1

*Work in progress:*
Depending on your location you can download 

## Requirements

- Python3 (optional: python3-venv)
```
# apt install python3-venv
```

- Geckodriver (for scraping 'timeanddate.com/moon/phases'):
```
# apt install firefox-geckodriver
```

- 7zip (for unpacking pictures of the moon):
```
# apt install p7zip-full
```

## Install

Clone this repository in your home directory

```
$ cd ~
$ git clone https://github.com/sguldemond/moon-paper
$ cd moon-paper
```

Download pictures of the moon
(http://neoprogrammics.com/ > Lunar Phase Image Sets > near_side_1024x1024X8.7z)

```
$ wget http://neoprogrammics.com/lunar_phase_images/downloads/near_side_1024x1024x8.7z
$ 7za x near_side_1024x1024x8.7z -o/home/$USER/moon-paper/images
```

Install python packages

```
$ (optional) python3 -m venv venv
$ (optional) source venv/bin/activate
$ pip install -r requirements.txt
```

Scrape moon phase data from timeanddate.com

```
$ python3 phase-scrapper.py > phase-schedule.json
```

Create schedule based on phases

```
$ python3 python3 daily_schedule.py > img-schedule.json
```

Finally create a cron job for replacing the wallpaper every 2 hours with the corresponding moon phase

```
$ python3 crontab_setter.py
```


## Sources

- https://commons.wikimedia.org/wiki/User:JayTanner/lunar-west-side-phase-set
- https://www.timeanddate.com/moon/phases/


## Notes

### Phase Orientation Legend

| Angle | Phase         | Eye View                           |
|-------|---------------|------------------------------------|
| 000   | New Moon      | Sun horizontally aligned with Moon |
| 090   | First Quarter | Sun directly to right              |
| 180   | Full Moon     | Sun directly behind                |
| 270   | Last Quarter  | Sun directly to left               |
| 360   | New Moon      | Sun horizontally aligned with Moon |

### Other

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
