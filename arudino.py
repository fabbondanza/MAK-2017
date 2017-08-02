import serial
import time

class MotorMove(object):
    def __init__(self, parent=None):
        self.arduino = serial.Serial('/dev/ttyACM0', 9600)
        if self.arduino is None:
            print 'Device not found'

    def _set_initial_position(self):
        self.arduino.write('(1,1)')
        motorStatus = 0
        while motorStatus == 0:
            status = self.arduino.readline()
            print status
            if status[0] == 'D':
                time.sleep(1); #Take Camera Reading
                motorStatus = 1
        self.currentWell = '1_12'

    def _get_current_position(self):
        self.arduino.write('X')
        positionX = int(self.arduino.readline())
        self.arduino.write('Y')
        positionY = int(self.arduino.readline())
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

    def _set_new_position(self,well):
        y_done = 0;
        x_done = 0;
        wellDistance = 60
        currentRow = int(self.currentWell.split('_')[0])
        currentCol = int(self.currentWell.split('_')[1])
        newRow = int(well.split('_')[0])
        newCol = int(well.split('_')[1])
        rowsToMove = int(newRow-currentRow)
        colsToMove = int(newCol-currentCol)
        currentX, currentY = self._get_current_position()
        if rowsToMove < 0:
            newY = currentY-(abs(rowsToMove*wellDistance))
            y_done = 1
        elif rowsToMove > 0:
            newY = currentY + (abs(rowsToMove*wellDistance))
            y_done = 1
        else:
            newY = currentY
            y_done = 1
        if colsToMove < 0:
            newX = currentX-(abs(colsToMove*wellDistance))
            x_done = 1
        elif colsToMove > 0:
            newX = currentX + (abs(colsToMove*wellDistance))
            x_done = 1
        else:
            newX = currentX
            x_done = 1
        if x_done == 1 & y_done == 1:
            newPosition = '('+str(newX)+','+str(newY)+')'

        return newPosition

    def _move_to_new_position(self,toReadNum):
        for well in toReadNum:
            motorStatus = 0
            newPosition = self._set_new_position(well)
            print newPosition
            self.currentWell = well
            self.arduino.write(newPosition)
            while motorStatus == 0:
                status = self.arduino.readline()
                if status[0] == 'D':
                    time.sleep(1)
                    #Take Camera Reading
                    motorStatus = 1


##m = MotorMove()
##m._set_initial_position()
##m._get_current_position()
##toReadNum = m._convert_labels_to_numericals(['B10','C12'])
##print toReadNum
##m._move_to_new_position(toReadNum)
##m.arduino.close() #NECESSARY TO MAINTAIN PROPER POTENTIOMETER VALUE CONVENTION

#toRead = ['A12']
#toReadNum = m._convert_labels_to_numericals(toRead)
#m._move_to_new_position(toReadNum)
