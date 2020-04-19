#/bin/bash

MP_FOLDER=/home/$USER/moon-paper

# Scrape moon phase data from timeanddate.com
python3 phase-scrapper.py > $MP_FOLDER/phase-schedule.json

# Create schedule based on phases
python3 daily_schedule.py > $MP_FOLDER/img-schedule.json

# Copy change_background script
cp change_background.py $MP_FOLDER/change_background.py

# Create a cron job for replacing the wallpaper every 2 hours with the corresponding moon phase
python3 crontab_setter.py

# Set the wallpaper for the first time
python3 $MP_FOLDER/change_background.py