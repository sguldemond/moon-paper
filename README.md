# Moon Paper

Update your wallpaper with the an image of the real time phase of the moon in your location.

![animate-moon](images/moon.gif)

Currently working with Ubuntu 19.10 running Gnome 3.34.1

Also had it working on Mate, see [change_background.py](change_background.py). By changing the calls from `gsettings` to `dconf` it should work for Mate.

## 📋 Requirements

- Python3 (optional: python3-venv)
```
# apt install python3 python3-venv
```

- Geckodriver (for scraping https://timeanddate.com/moon/phases):
```
# apt install firefox-geckodriver
```

- 7zip (for unpacking pictures of the moon):
```
# apt install p7zip-full
```

## 🔧 Install

**Clone this repository**

```
$ cd ~
$ git clone https://github.com/sguldemond/moon-paper
$ cd moon-paper
```

**Setup folder for in home directory**
```
$ mkdir ~/moon-paper
```

**Download pictures of the moon**

http://neoprogrammics.com/ > Lunar Phase Image Sets > near_side_1024x1024X8.7z

_or_

```
$ wget http://neoprogrammics.com/lunar_phase_images/downloads/near_side_1024x1024x8.7z
```

**Extract the images**

```
$ 7za x near_side_1024x1024x8.7z -o/home/$USER/moon-paper/images
```

**Install python requirements**

```
$ (optional) python3 -m venv venv
$ (optional) source venv/bin/activate
$ pip install -r requirements.txt
```

**Setup and install**

```
# chmod +x setup_and_install.sh
# ./setup_and_install.sh
```

_Look inside this shell script to see the different steps taken._


Now your background should be changed to the current phase of the moon in your location and will update every 2 hours.

**Enjoy and get in sync with the moon!**


## 🌐 Sources

- http://www.neoprogrammics.com/lunar_phase_images/ (Images licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/]))
- https://www.timeanddate.com/moon/phases/
- https://commons.wikimedia.org/wiki/User:JayTanner/lunar-west-side-phase-set


## 🌘 Phase Orientation Legend

| Angle | Phase         | Eye View                           |
|-------|---------------|------------------------------------|
| 000   | New Moon      | Sun horizontally aligned with Moon |
| 090   | First Quarter | Sun directly to right              |
| 180   | Full Moon     | Sun directly behind                |
| 270   | Last Quarter  | Sun directly to left               |
| 360   | New Moon      | Sun horizontally aligned with Moon |

## 🎞️ Moon GIF

Images used:
http://neoprogrammics.com/lunar_phase_images/downloads/near_side_256x256x8.7z

**Create GIF**

```
# apt install imagemagick
$ convert -delay 10 -loop 1 *.png moon.gif
$ animate moon.gif
```

## 📓 Notes

List all cron jobs (of current user)
```
crontab -l
```

Edit cron jobs to remove background update
```
crontab -e
```

Bash without profile
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
