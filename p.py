#!/usr/bin/env python

from gpiozero import LED
from time import sleep

led = LED(17)

led.on()
sleep(0.25)
led.off()
for x in range(0, 2):
    led.on()
    sleep(0.5)
    led.off()
    sleep(0.25)
led.on()
sleep(0.25)
led.off()
