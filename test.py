import usb.core
import usb.util
import sys
import binascii
import numpy as np
interface = 0
dev = usb.core.find(idVendor=0x04B4, idProduct=0x0328)
string = ''

if dev is None:
    print "device not found"
else:
    print "device found"
    dev.set_configuration(1)
    usb.util.claim_interface(dev,interface)
    cmnd_setmode = '\x38\x01\16'
    cmnd_frameinfo = '\x33\x01\x00'
    cmnd_getdata = '\x34\x02\x10'
    cmnd_info = '\x21\x01\x00'
    cmnd_firmware ='\x01\x01\x02'
    ep = dev[0][(0,0)][0]

    ep.write(cmnd_firmware,1)
    #ep.write(cmnd_setmode,1)
    #ep.write(cmnd_frameinfo)
    #ep.write(cmnd_getdata,1)
    #ep.write(cmnd_info,1)

    firmware = dev.read(0x81, ep.wMaxPacketSize)
    #frames = dev.read(0x81,ep.wMaxPacketSize)
    #print frames

    #info = dev.read(0x81,ep.wMaxPacketSize)
    #print info

    #data = dev.read(0x82,ep.wMaxPacketSize)
    #print data
        

    dev.reset()
    
    
    


