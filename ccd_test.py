#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as pl
from camera import *
from arudino import *
import csv

c = LineCamera()
# m = MotorMove()
print('Firmware version', c.get_firmware_ver())
print('Device version', c.get_device_info())
c.set_work_mode(WorkMode.NORMAL)
c.set_exposure_time(1)

def read_frame():
    try: frame = c.get_frame()
    except: return None
    if frame is not None:
        return frame.image #- np.mean(frame.dark)
    else:
        return None

fig = pl.figure()
ax = fig.add_subplot(111)
curve, = ax.plot([], [])
ax.set_ylim(-10, 0xffff+10)
ax.set_ylim(-10, 10000)
ax.set_xlim(0, 3648)
ax.axvline(x=1824, color='r')

def update():
    global i
    i += 1
    data = read_frame()
    if i == 20:
        with open('Rho30uM.csv', 'w') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for k in data:
                spamwriter.writerow([str(k)])

    if data is None: return True
    x = np.arange(len(data))
    print data
    curve.set_data(x, data)
    fig.canvas.draw()


read_frame()
i = 0
# m._toggle_led('B')
timer = fig.canvas.new_timer(interval=100)
timer.add_callback(update)
timer.start()
pl.show()
