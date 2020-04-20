import change_background
import subprocess
import time

time.sleep(5)

for i in range(0, 360):
    change_background.set_background(i)
    time.sleep(1)
    subprocess.call(['import', '-window', 'root', 'screenshot-{}.png'.format(i)])
    print(i)
