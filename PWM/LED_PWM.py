#!/usr/bin/env python
import time
import RPi.GPIO as GPIO
import sys

# PWM GPIO init
PWM_PIN_RED = 11
PWM_PIN_GREEN = 13
PWM_PIN_BLUE = 15
PWM_FREQ = 500

GPIO.setmode(GPIO.BOARD)
GPIO.setup(PWM_PIN_RED, GPIO.OUT)
GPIO.setup(PWM_PIN_GREEN, GPIO.OUT)
GPIO.setup(PWM_PIN_BLUE, GPIO.OUT)
PWM_Process_RED = GPIO.PWM(PWM_PIN_RED, PWM_FREQ)  # channel=11 frequency=50Hz
PWM_Process_GREEN = GPIO.PWM(PWM_PIN_GREEN, PWM_FREQ)  # channel=13 frequency=50Hz
PWM_Process_BLUE = GPIO.PWM(PWM_PIN_BLUE, PWM_FREQ)  # channel=15 frequency=50Hz


# test part
PWM_Process_RED.start(0)
PWM_Process_GREEN.start(0)
PWM_Process_BLUE.start(0)
try:
    while 1:
        for dc in range(0, 101, 5):
            PWM_Process_RED.ChangeDutyCycle(dc)
            PWM_Process_GREEN.ChangeDutyCycle(dc)
            PWM_Process_BLUE.ChangeDutyCycle(dc)
            time.sleep(0.1)
            print("inc"+str(dc))
        for dc in range(100, -1, -5):
            PWM_Process_RED.ChangeDutyCycle(dc)
            PWM_Process_GREEN.ChangeDutyCycle(dc)
            PWM_Process_BLUE.ChangeDutyCycle(dc)
            time.sleep(0.1)
            print("dec"+str(dc))
except KeyboardInterrupt:
    pass
PWM_Process_RED.stop()
GPIO.cleanup()


# ############### main function #############

# def Set_PWMLED(value1, value2, value3):
# 	PWM_Process_RED.ChangeDutyCycle(value1)
# 	PWM_Process_GREEN.ChangeDutyCycle(value2)
# 	PWM_Process_BLUE.ChangeDutyCycle(value3)

# def Stop_PWMLED():
# 	PWM_Process_RED.ChangeDutyCycle(0)
# 	PWM_Process_GREEN.ChangeDutyCycle(0)
# 	PWM_Process_BLUE.ChangeDutyCycle(0)

# # stat PWM with 0 % output
# PWM_Process_RED.start(0)
# PWM_Process_GREEN.start(0)
# PWM_Process_BLUE.start(0)

# print('Number of arguments:', len(sys.argv), 'arguments.')
# print('Argument List:', str(sys.argv))
# PWM_ReceivedCommend = sys.argv
# PWM_ReceivedCommend.remove(PWM_ReceivedCommend[0])
# PWM_LEDCommend=[0,0,0]

# try:
# 	for x in range(0, 3):
# 		val = float(PWM_ReceivedCommend[x])
# except ValueError:
# 	print("That's not an float value!")

# if (PWM_ReceivedCommend[0] is '0' and PWM_ReceivedCommend[1] is '0' and PWM_ReceivedCommend[2] is '0'):
# 	print("Stop LED")
# 	try:
# 		Stop_PWMLED()
# 	except ValueError:
# 		print("StopLED error")
# 	sleep(1)
# else:
# 	print(PWM_ReceivedCommend)
# 	PWM_LEDCommend[0] = float(PWM_ReceivedCommend[0])
# 	PWM_LEDCommend[1] = float(PWM_ReceivedCommend[1])
# 	PWM_LEDCommend[2] = float(PWM_ReceivedCommend[2])
# 	print("PWM_ReceivedCommend : " + str(PWM_LEDCommend))
# 	try:
# 		Set_PWMLED(PWM_LEDCommend[0], PWM_LEDCommend[1], PWM_LEDCommend[2])
# 	except ValueError:
# 		print("PWM_LEDCommend error")
# 	sleep(1)

# print("End program")

# PWM_Process_RED.stop()
# PWM_Process_GREEN.stop()
# PWM_Process_BLUE.stop()
# GPIO.cleanup()
