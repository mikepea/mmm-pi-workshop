#!/usr/bin/env python

red_pin = 11
whi_pin = 12

l_pin = 13
r_pin = 15

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(whi_pin, GPIO.OUT)
GPIO.setup(l_pin, GPIO.OUT)
GPIO.setup(r_pin, GPIO.OUT)

while True:
    GPIO.output(red_pin, True)
    GPIO.output(whi_pin, False)
    GPIO.output(l_pin, True)
    GPIO.output(r_pin, False)
    sleep(1.0)
    GPIO.output(red_pin, False)
    GPIO.output(whi_pin, True)
    GPIO.output(l_pin, False)
    GPIO.output(r_pin, True)
    sleep(1.0)
