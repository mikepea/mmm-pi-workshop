#!/usr/bin/python

pin = 11

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

GPIO.setup(pin, GPIO.OUT)

GPIO.output(pin, True)

sleep(5)

GPIO.output(pin,False)

sleep(5)
