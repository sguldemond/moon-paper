from datetime import datetime, timedelta
import json
import time

fmt = '%Y-%m-%d %H:%M'

with open('./phase-schedule.json', 'r') as f:
    phase_json = f.read()
    phase_schedule = json.loads(phase_json)

between_minutes = []
schedule = []

for i in range(len(phase_schedule)):
    # break at end
    if i == len(phase_schedule)-1:
        break

    d1_str = phase_schedule[i].get('date_time')
    d2_str = phase_schedule[i+1].get('date_time')

    d1 = datetime.strptime(d1_str, fmt)
    d2 = datetime.strptime(d2_str, fmt)

    d1_ts = time.mktime(d1.timetuple())
    d2_ts = time.mktime(d2.timetuple())

    min_diff = int(d2_ts-d1_ts) / 60
    avg_diff = min_diff / 90
    
    img_id = phase_schedule[i].get('image_id')
    angle = int(img_id)

    tick = {
        'time': d1_str,
        'angle': angle
    }

    schedule.append(tick)

    new_time = d1
    angle = angle + 1
    for i in range(90):
        new_time = new_time + timedelta(minutes=avg_diff)

        tick = {
            'time': new_time.strftime(fmt),
            'angle': angle + i
        }

        schedule.append(tick)
    
print(json.dumps(schedule))