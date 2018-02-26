#!/usr/bin/env python

from gpiozero import LED
from time import sleep

led = LED(17)

for x in range(0, 3):
    led.on()
    sleep(0.5)
    led.off()
    sleep(0.25)
