#!/usr/bin/python

pin = 11

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

GPIO.setup(pin, GPIO.OUT)

while True:
    GPIO.output(pin, True)
    sleep(0.1)
    GPIO.output(pin,False)
    sleep(0.1)
