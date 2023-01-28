from machine import Pin, PWM
import utime

class Engine:
    def __int__(self, forward, backward, speed):
        self.forward = forward
        self.backward = backward
        self.speed = speed
        speed.freq(1000)
        speed.duty_u16(int(65535 * 0.5))

    def forward(self):
       self.backward.off()
       self.forward.on()


led = Pin(25)
led.on()
left_engine = Engine(Pin(0), Pin(2), PWM(Pin(4)))
right_engine = Engine(Pin(5), Pin(18), PWM(Pin(19)))

