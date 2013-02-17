#!/usr/bin/env python

r_pin = 11
w_pin = 12
button_pin = 22

import RPi.GPIO as GPIO
from time import sleep

import time as time_

def millis():
    return int(round(time_.time() * 1000))

GPIO.setmode(GPIO.BOARD)

GPIO.setup(r_pin, GPIO.OUT)
GPIO.setup(w_pin, GPIO.OUT)
GPIO.setup(button_pin, GPIO.IN)

last = False
pressed = False

r_timer = 0
r_on = False
w_timer = 0
w_on = False

while True:
  input = GPIO.input(button_pin)
  if (input and input != last):
    print "button pressed!"
    print millis()
    r_on = True
    w_on = True
    r_timer = millis()
    w_timer = millis()

  if millis() - r_timer > 500:
    r_on = False

  if millis() - w_timer > 1000:
    w_on = False

  if r_on:
    GPIO.output(r_pin, True)
  else:
    GPIO.output(r_pin, False)

  if w_on:
    GPIO.output(w_pin, True)
  else:
    GPIO.output(w_pin,False)

  last = input
 

