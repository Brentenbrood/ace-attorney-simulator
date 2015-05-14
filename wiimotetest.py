#-------------------------------------------------------------------------------
# Name:        Wii Remote - connect to Bluetooth cwiid
# Purpose:
#
# Author:      Brian Hensley
#
# Created:     21/07/2012
# Copyright:   (c) Brian 2012
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import cwiid
import time
import pygame

def main():

        print 'Press button 1 + 2 on your Wii Remote...'
        time.sleep(1)

        wm=cwiid.Wiimote()
        print 'Wii Remote connected...'
        print '\nPress the PLUS button to disconnect the Wii and end the application'
        time.sleep(1)
	
        Rumble = False
        wm.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC
        wm.led = 1

        while True:
            if wm.state['acc'][2] <= 40:
                print 'SLAM'
                time.sleep(.3)

            if wm.state['acc'][1] <= 50:
                print 'OBJECTION!'
                time.sleep(.3)

            if wm.state['buttons'] == 512:
                position = 50
                print 'Position: ', position
                time.sleep(.5)

            while wm.state['buttons'] == 8:
                print(wm.state)
                time.sleep(0.3)

            if wm.state['buttons'] == 2:
                print 'Button 1 pressed'
                time.sleep(.5)

            if wm.state['buttons'] == 1:
                print 'Button 2 pressed'
                time.sleep(.5)
            if wm.state['buttons'] == 16:
                if Rumble == False:
                    wm.rumble = True
                    Rumble = True
                    time.sleep(1)
                elif Rumble == True:
                    wm.rumble = False
                    Rumble = False
                    time.sleep(1)
            if wm.state['buttons'] == 4096:
                print 'closing Bluetooth connection. Good Bye!'
                time.sleep(1)
                exit(wm)


if __name__ == '__main__':
    main()

