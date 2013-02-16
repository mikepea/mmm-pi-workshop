#!/usr/bin/env python

r_pin = 11
w_pin = 12

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

GPIO.setup(r_pin, GPIO.OUT)
GPIO.setup(w_pin, GPIO.OUT)

while True:
    GPIO.output(r_pin, True)
    sleep(0.1)
    GPIO.output(r_pin,False)
    sleep(0.1)
    GPIO.output(w_pin, True)
    sleep(0.1)
    GPIO.output(w_pin,False)
    sleep(0.1)
