from machine import Pin, PWM
import utime

l1 = Pin(0, Pin.OUT)
l2 = Pin(2, Pin.OUT)
ls = PWM(Pin(4, Pin.OUT))
r1 = Pin(5, Pin.OUT)
r2 = Pin(18, Pin.OUT)
rs = PWM(Pin(19, Pin.OUT))

ls.freq(1000)
ls.duty_u16(65535)
rs.freq(1000)
rs.duty_u16(65535)

led1 = Pin(21, Pin.OUT)
led2 = Pin(20, Pin.OUT)
led3 = Pin(25, Pin.OUT)

for x in range(10):
    led3.value((x+1) % 2)
    utime.sleep(1)

l1.on()
l2.off()
r1.on()
r2.off()
utime.sleep(5)

r1.off()
r2.on()

utime.sleep(1)

l1.off()
l2.on()

utime.sleep(5)

ls.duty_u16(32767)
rs.duty_u16(32767)

l1.on()
l2.off()

utime.sleep(1)

l1.off()
l2.off()
r1.off()
r2.off()

for x in range(20):
    led3.value((x+1) % 2)
    utime.sleep(0.1)
