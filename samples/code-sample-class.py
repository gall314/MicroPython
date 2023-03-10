from machine import Pin, PWM
import utime


class Engine:
    def __init__(self, forward, backward, speed):
        self.forward = forward
        self.backward = backward
        self.speed = speed
        speed.freq(1000)
        speed.duty_u16(int(65535 * 0.5))

    def move_forward(self):
        self.forward.on()
        self.backward.off()


led = Pin(25)
led.on()
left_engine = Engine(Pin(0), Pin(2), PWM(Pin(4)))
right_engine = Engine(Pin(5), Pin(18), PWM(Pin(19)))

left_engine.move_forward()
