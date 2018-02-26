#!/usr/bin/env python

from gpiozero import LED
from time import sleep


def beep(time, wait):
    led = LED(17)
    led.On()
    sleep(time)
    led.Off()
    sleep(wait)
