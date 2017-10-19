from ctypes import *

mydll = cdll.LoadLibrary("C:\Users\LokoKoko\Desktop\LAC\mpusbapi.dll")
deviceVID_PID = "vid_04d8&pid_fc5f"

ACTUATORPOSValue = c_uint16(0)
# ACTUATORSPDValue = 1023, ACTUATORextendstallValue = 10, ACTUATORControl_maxValue = 1023,
#          ACTUATORPos_ThresholdValue = 4,
#          ACTUATORMovement_ThresholdValue = 3,
#          ACTUATORControl_minValue = 0,
#          ACTUATORStall_timeValue = 10000,
#          ACTUATORPWM_ThresholdValue = 80,
#          ACTUATORAverage_adcValue = 8,
#          ACTUATORKpValue = 1,
#          ACTUATORAverage_RCValue = 4,
#          ACTUATORPWM_maxValue = 1023,
#          ACTUATORKdValue = 10,
#          ACTUATORPWM_minValue = 80,
#          ACTUATORDerivative_maxValue = 1023,
#          ACTUATORDerivative_minValue = 0)
# print hm

AttachedState = c_bool(False)
# ACTUATORPOSFlag = False, ACTUATORSPDFlag = False, ACTUATORControl_maxFlag = False,
#        ACTUATORPos_ThresholdFlag = False,
#        ACTUATORMovement_ThresholdFlag = False,
#        ACTUATORControl_minFlag = False,
#        ACTUATORPWM_ThresholdFlag = False,
#        ACTUATORAverage_adcFlag = False,
#        ACTUATORKpFlag = False,
#        ACTUATORextendstallFlag = False,
#        ACTUATORAverage_RCFlag = False,
#        ACTUATORPWM_maxFlag = False,
#        ACTUATORKdFlag = False,
#        ACTUATORPWM_minFlag=False,
#        ACTUATORDerivative_maxFlag = False,
#        ACTUATORDerivative_ThresholdFlag = False,
#        ACTUATORDerivative_minFlag = False,
#        buttonResetFlag = False,
#        buttonSave_ConfigFlag = False,
#        button_cycletestFlag = False,
#        buttonEnable_RC_ProgFlag = False,
#        buttonDisable_RC_ProgFlag = False)

# #####----- Initial Start up -------#######
if mydll._MPUSBGetDeviceCount(deviceVID_PID) == 1:
    EP1OUTHandle = mydll._MPUSBOpen(0, deviceVID_PID, "\MCHP_EP1", 0, 0);
    EP1INHandle = mydll._MPUSBOpen(0, deviceVID_PID, "\MCHP_EP1", 1, 0);

    AttachedState = True

bufferVar = create_string_buffer(64)
actualLength = 0
c_ulong(actualLength)
tempPos = c_uint16(100)
while(True):
    ACTUATORPOSFlag = True
    if ACTUATORPOSFlag == True:
        tempPos = ACTUATORPOSValue
        bufferVar[0] = '\x20'
        bufferVar[1] = '\x01'
        bufferVar[2] = '\x03'

        if AttachedState == True:
            if mydll._MPUSBWrite(EP1OUTHandle, bufferVar, 3, actualLength, 1000) == 1:
                if mydll._MPUSBRead(EP1INHandle, bufferVar, 3, actualLength, 1000) == 1:
                    print bufferVar[1]



# nelem = 1

# actualLength = 0
# c_ulong(actualLength)
# print sizeof(Buf) , repr(Buf.raw)
# value = 0
# Buf[0] = '\x20'
# Buf[1] = c_char('\x00')
# Buf[2] = c_char('\x00')
#
#
# mydll._MPUSBRead(devIn,Buf, 3, actualLength)
#
#
