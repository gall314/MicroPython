from machine import Pin, PWM
import utime

pwm = PWM(Pin(25))
pwm.freq(100)

duty = 0
direction = 1

for _ in range(800 * 256):
    duty += direction
    if duty > 255:
        duty = 255
        direction = -1
    elif duty < 0:
        duty = 0
        direction = 1
    pwm.duty_u16(duty * duty)
    if duty == 0:
        utime.sleep(0.2)
    else:
        utime.sleep(0.001)

