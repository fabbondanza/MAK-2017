import time
import warnings
import serial
import serial.tools.list_ports



class MotorMove(object):
    def __init__(self, parent=None):
        ser_ports = [
            p.device
            for p in serial.tools.list_ports.comports()
            if 'Arduino' in p.description
        ]
        if not ser_ports:
            raise IOError("No ser found")
        else:
            self.ser = serial.Serial(ser_ports[0], 9600)
        if len(ser_ports) > 1:
            warnings.warn('Multiple sers found - using the first')
        time.sleep(5)
        if self.ser is None:
            print 'Device not found'
        # self.ser = serial.Serial('/dev/ttyACM0', 9600)

    def _set_opening_position(self):
        print 'Moving to opening position...'
        self.ser.write('M1023,1023')
        self.motorStatus = 0
        while motorStatus == 0:
            status = self.ser.readline()
            print status
            if status[0] == 'D':
                motorStatus = 1
        print 'Insert Plate'

    def _set_initial_position(self):
        print 'Moving to initial position...'
        self.ser.write('M30,30')
        self.motorStatus = 0
        while self.motorStatus == 0:
            status = self.ser.readline()
            print status
            if status[0] == 'D':
                self.motorStatus = 1
        print 'Read to take measurement...'
        time.sleep(1)

    def _set_blank_position(self, blankPositionStr, blankPosition):
        print 'Moving to Blank position...'
        self.ser.write(blankPosition)
        self.motorStatus = 0
        while self.motorStatus == 0:
            status = self.ser.readline()
            print status
            if status[0] == 'D':
                self.motorStatus = 1
        print 'Read to take measurement...'
        time.sleep(1)

    def _set_new_position(self, well, wellPosition):
        print 'Moving to' + well
        self.ser.write(wellPosition)
        self.motorStatus = 0
        while self.motorStatus == 0:
            status = self.ser.readline()
            print status
            if status[0] == 'D':
                self.motorStatus = 1
        self.currentWell = well
        time.sleep(1)

    def _get_current_position(self):
        self.ser.write('X')
        positionX = int(self.ser.readline())
        self.ser.write('Y')
        positionY = int(self.ser.readline())
        return positionX, positionY

    def _convert_labels_to_numericals(self, toRead):
        well_letters = ['A','B','C','D','E','F','G','H']
        toReadNum = []
        for well in toRead:
            wellRow = well[0]
            wellCol = int(well[1:len(well)])
            for index in range(0,len(well_letters)):
                if wellRow == well_letters[index]:
                    toReadNum.append(str(index+1)+'_'+ str(wellCol))

        return toReadNum

    # def _set_new_position(self,well):
    #     y_done = 0
    #     x_done = 0
    #     wellDistanceY = 94
    #     wellDistanceX = 94
    #     currentRow = int(self.currentWell.split('_')[0])
    #     currentCol = int(self.currentWell.split('_')[1])
    #     newRow = int(well.split('_')[0])
    #     print 'newRow: ', newRow
    #     newCol = int(well.split('_')[1])
    #     rowsToMove = int(newRow-currentRow)
    #     colsToMove = int(newCol-currentCol)
    #     currentX, currentY = self._get_current_position()
    #     if rowsToMove < 0:
    #         newY = currentY-(abs(rowsToMove*wellDistanceY))
    #         if newY < 0:
    #             newY = 0
    #         y_done = 1
    #     elif rowsToMove > 0:
    #         newY = currentY + (abs(rowsToMove*wellDistanceY))
    #         if newY < 0:
    #             newY = 0
    #         y_done = 1
    #     else:
    #         newY = currentY
    #         y_done = 1
    #     if colsToMove < 0:
    #         newX = currentX-(abs(colsToMove*wellDistanceX))
    #         x_done = 1
    #     elif colsToMove > 0:
    #         newX = currentX + (abs(colsToMove*wellDistanceX))
    #         x_done = 1
    #     else:
    #         newX = currentX
    #         x_done = 1
    #     if x_done == 1 & y_done == 1:
    #         newPosition = 'M'+str(abs(newX))+','+str(newY)
    #     return newPosition

    def _move_to_new_position(self,well):
        motorStatus = 0
        newPosition = self._set_new_position(well)
        print newPosition
        self.currentWell = well
        self.ser.write(newPosition)
        while motorStatus == 0:
            status = self.ser.readline()
            if status[0] == 'D':
                time.sleep(1)
                #Take Camera Reading
                motorStatus = 1
                return motorStatus
    def _set_led_in_position(self,color):
        self.ser.write('S'+color)
    def _toggle_led(self,color):
        self.ser.write('L'+color)
        time.sleep(1)
#m = MotorMove()
#m._set_initial_position()
#m._get_current_position()
#toReadNum = m._convert_labels_to_numericals(['B10','C12'])
##print toReadNum
##m._move_to_new_position(toReadNum)
##m.ser.close() #NECESSARY TO MAINTAIN PROPER POTENTIOMETER VALUE CONVENTION

#toRead = ['A12']
#toReadNum = m._convert_labels_to_numericals(toRead)
#m._move_to_new_position(toReadNum)
