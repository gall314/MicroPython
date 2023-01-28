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

# blink led for 5 times with 1 second delay
for x in range(10):
    led3.value((x+1) % 2)
    utime.sleep(1)

# forward for 5 seconds with 100% speed
l1.on()
l2.off()
r1.on()
r2.off()
utime.sleep(5)

# turn left for 1 second with 100% speed
# l1.on()
# l2.off()
r1.off()
r2.on()

utime.sleep(1)

# backward for 5 seconds with 100% speed
l1.off()
l2.on()
# r1.off()  # it's already off
# r2.on()   # it's already on

utime.sleep(5)

# turn left for 1 second with 50% speed
ls.duty_u16(32767)
rs.duty_u16(32767)

l1.on()
l2.off()
# r1.off()  # it's already off
# r2.on()   # it's already on

utime.sleep(1)

# stop
l1.off()
l2.off()
r1.off()
r2.off()

# blink led for 10 times with 0.1 second delay
for x in range(20):
    led3.value((x+1) % 2)
    utime.sleep(0.1)

