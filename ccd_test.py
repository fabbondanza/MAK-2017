import numpy as np
import matplotlib.pyplot as pl
from mightex import *
import csv
import time
import threading
from arudinoPi_demos import *
from threading import Timer,Thread,Event

c = LineCamera()
# m = MotorMove()
print('Firmware version', c.get_firmware_ver())
print('Device version', c.get_device_info())
c.set_work_mode(WorkMode.NORMAL)
c.set_exposure_time(8)


# def read_frame():
#     for i in range(0, 1):
#         frame = c.get_frame()
#     return frame.image

def read_frame():
    try:
        frame = c.get_frame()
    except:
        return None
    if frame is not None:
        return frame.image # - np.mean(frame.dark)
    else:
        return None


fig = pl.figure()
ax = fig.add_subplot(111)
curve, = ax.plot([], [])
ax.set_ylim(-10, 0xffff + 10)
ax.set_xlim(0, 3648)
ax.axvline(x=1824, color='r')


def update():
    data = read_frame()
    row = []
    if data is None: return True
    else:
        x = np.arange(len(data))
        curve.set_data(x, data)
        fig.canvas.draw()
    # with open('EL222_test_functionality.csv', 'ab') as csvfile:
    #     spamwriter = csv.writer(csvfile, delimiter=',',
    #                             quotechar='|', quoting=csv.QUOTE_MINIMAL)
    #     spamwriter.writerow(row)
    #     print 'Added'
    # csvfile.close()

class perpetualTimer():

   def __init__(self,t,hFunction):
      self.t=t
      self.hFunction = hFunction
      self.thread = Timer(self.t,self.handle_function)

   def handle_function(self):
      self.hFunction()
      self.thread = Timer(self.t,self.handle_function)
      self.thread.start()

   def start(self):
      self.thread.start()

   def cancel(self):
      self.thread.cancel()


with open('EL222_test_functionality.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['KAM-Spec 2017'])
    spamwriter.writerow(['Date:', time.strftime('%m/%d/%Y')])
    spamwriter.writerow(['Time:', time.strftime('%H:%M:%S')])
    spamwriter.writerow([' '])
    spamwriter.writerow([' '])
    spamwriter.writerow([' '])
    spamwriter.writerow([' '])
    spamwriter.writerow(['EL222'])
csvfile.close()
# m._set_initial_position()
read_frame()
# t = perpetualTimer(5,update)
# t.start()
timer = fig.canvas.new_timer(interval=100)
timer.add_callback(update)
timer.start()
fig.canvas.show()
pl.show()