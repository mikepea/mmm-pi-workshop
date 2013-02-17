#!/usr/bin/env python 

from subprocess import call, check_output
from time import sleep

call('rmmod w1-therm', shell=True)
call('rmmod w1-gpio', shell=True)

sleep(1.0)

call('modprobe w1-gpio', shell=True)
call('modprobe w1-therm', shell=True)

dir = check_output("ls -d /sys/bus/w1/devices/10-*", shell=True).rstrip('\n')

tfile = open(dir + "/w1_slave") 

text = tfile.read() 

tfile.close()

secondline = text.split("\n")[1]
temp = secondline.split(" ")[9][2:]

print temp
