import subprocess
import datetime
import json
import getpass

user = getpass.getuser()

def set_angle():
    fmt = '%Y-%m-%d %H:%M'

    now = datetime.datetime.now()

    with open("/home/{user}/moon-paper/img-schedule.json".format(user=user), 'r') as f:
        schedule_json = f.read()
        img_schedule = json.loads(schedule_json)

    times = [datetime.datetime.strptime(s.get('time'), fmt) for s in img_schedule]

    # abs(x - y) gets distance between two dates, as timedelta (seconds)
    # lambda defines function where d is extracted for every item in list
    # min gets the smallest value (timedelta/seconds)
    closest = min(times, key=lambda d: abs(d - now))
    closest_str = closest.strftime(fmt)

    item = list(filter(lambda x: x.get('time') == closest_str, img_schedule))[0]

    set_background(item.get('angle'))

def set_background(pic_id):
    pic_base = "/home/{user}/moon-paper/images/near_side_1024x1024x8/{id}.png"
    pic_file = pic_base.format(user=user, id=str(pic_id).zfill(3))

    write_gsettings(option='picture-options', value='centered')
    write_gsettings(option='picture-uri', value=pic_file)

    # write_dconf(option='picture-options', value='centered')
    # write_dconf(option='picture-filename', value=pic_file)

# For Mate environment
def write_dconf(option, value):
    full_option = '/org/mate/desktop/background/{}'.format(option)
    print(['dconf', 'write', full_option, "'{}'".format(value)])
    subprocess.call(['dconf', 'write', full_option, "'{}'".format(value)])

# For Gnome environment
def write_gsettings(option, value):
    background_key = "org.gnome.desktop.background"
    print(['gsettings', 'set', background_key, option, value])
    subprocess.call(['gsettings', 'set', background_key, option, value])


# set_background(90)
# print("Done setting background!")

set_angle()