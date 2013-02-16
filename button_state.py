#!/usr/bin/env python

r_pin = 11
w_pin = 12
button_pin = 22

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

GPIO.setup(r_pin, GPIO.OUT)
GPIO.setup(w_pin, GPIO.OUT)
GPIO.setup(button_pin, GPIO.IN)

last = False

while True:
  input = GPIO.input(button_pin)
  if (input and input != last):
    print "button pressed!"
    GPIO.output(r_pin, True)
    sleep(0.1)
    GPIO.output(r_pin,False)
    sleep(0.1)
    GPIO.output(w_pin, True)
    sleep(0.1)
    GPIO.output(w_pin,False)
    sleep(0.1)

  last = input
 

