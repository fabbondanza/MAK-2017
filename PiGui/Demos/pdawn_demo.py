#### The following demo code is used to demonstrate the device performing a pDawn blue light activation time course.
## In the demo, pDawn is exposed to BLUE LIGHT while being shaken by the device. Shaking is defined as motion back &
## forth on the y-axis in this case. Every 30 minutes, the device will stop shaking, position itself of the detector
## region, turn-off the blue light, and quickly turn on the green light, to measure the flourescence of dsRed, a
## flourescent reporter protein. The data will be stored and the device will go back to shaking with a blue light on
## until the next time point.

from arudinoPiServo import *
from mightex import *
import time
import csv

def initializeCamera(camera):
    camera.set_work_mode(WorkMode.NORMAL)
    camera.set_exposure_time(25)
    return 25

def exposureCalibration(camera, machine, exposureTime):
    machine._set_initial_position()
    time.sleep(1)
    machine._toggle_led('W')
    time.sleep(1)
    counter = 0
    while counter == 0:
        data = read_frame(camera)
        time.sleep(.5)
        max = np.max(data)
        print 'Max: ' + str(max)
        if max > 55000:
            if exposureTime > 5:
                exposureTime = exposureTime - 5
            elif exposureTime <= 5 and exposureTime > 1:
                exposureTime = exposureTime - 1
            elif exposureTime == 1:
                exposureTime = exposureTime - 1 / float(10)
            elif exposureTime == 1 / float(10):
                print 'Low Reached'
            print 'New ET: ' + str(float(exposureTime))
            camera.set_exposure_time(exposureTime)
            time.sleep(.5)
        elif max < 1000:
            print 'Too Low'
        else:
            counter = 1
            print 'Done'
    return exposureTime

def timeCourseProtocol(timeInterval, exposureTime, totalDuration):
    machine._set_initial_position()
    time.sleep(3)
    machine._toggle_led('B')
    startTime = time.clock()
    


camera = LineCamera()
machine = MachineControl()