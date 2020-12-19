#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
from picamera import PiCamera

if __name__ == '__main__':
    # kick off the feeding process (move the servo)
    # we now use our new feedByGmail method to handle the feeding
    # feedByGmail()
    #feed()
    camera = PiCamera()
    camera.rotation = 180
    camera.start_preview()
    camera.capture('./server/static/img/live.jpg')
    camera.stop_preview()

