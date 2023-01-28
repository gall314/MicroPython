from machine import Pin, PWM
import utime

led = Pin(25, Pin.OUT)

for i in range(60):
    if i == 5:
        led.on()
    if i == 30:
        led.off()
