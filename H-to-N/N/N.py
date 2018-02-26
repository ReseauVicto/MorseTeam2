from gpiozero import LED
led = LED(17)


led.on()
sleep(0.5)
led.off()
sleep(0.25)

led.on()
sleep(0.25)
led.off()
sleep(0.25)
