#!/usr/bin/env python
import time
import RPi.GPIO as GPIO
import sys

# PWM GPIO init
PWM_PIN_RED = 11
PWM_PIN_GREEN = 13
PWM_PIN_BLUE = 15
PWM_FREQ = 50

# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(PWM_PIN_RED, GPIO.OUT)
# GPIO.setup(PWM_PIN_GREEN, GPIO.OUT)
# GPIO.setup(PWM_PIN_BLUE, GPIO.OUT)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)

try:
    while 1:
        dc = 100
        GPIO.output(11,GPIO.HIGH)
        GPIO.output(13,GPIO.HIGH)
        GPIO.output(15,GPIO.HIGH)
        time.sleep(3)
        dc = 0
        GPIO.output(11,GPIO.LOW)
        GPIO.output(13,GPIO.LOW)
        GPIO.output(15,GPIO.LOW)
        time.sleep(3)
except KeyboardInterrupt:
    pass
PWM_Process_RED.stop()
GPIO.cleanup()

