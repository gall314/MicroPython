from machine import Pin, PWM


class Motor:
    def __init__(self, forward, backward, speed):
        # Initialize the motor, input pins, and PWM (speed)
        self.pin_forward = Pin(forward, Pin.OUT)
        self.pin_backward = Pin(backward, Pin.OUT)
        self.pwm = PWM(Pin(speed))
        self.speed = 0
        # Set the PWM frequency to 1000Hz
        self.pwm.freq(1000)
        # Set the PWM duty cycle to 0 (off)
        self.pwm.duty_u16(0)

    def speed(self, speed):
        if abs(speed) < 0.1:
            self.speed = 0
            self.pwm.duty_u16(0)
            return
        if speed > 0:
            self.pin_forward.on()
            self.pin_backward.off()
        else:
            self.pin_forward.off()
            self.pin_backward.on()
        # ensure speed is between -100 and 100
        speed = max(-100, min(100, speed))
        # convert float from -100 to 100 to int from 0 to 65535
        self.pwm.duty_u16(int(abs(speed) * 655.35))

    def stop(self):
        self.pwm.duty_u16(0)
        self.pin_forward.off()
        self.pin_backward.off()

    def forward(self):
        self.pin_forward.on()
        self.pin_backward.off()

    def backward(self):
        self.pin_forward.off()
        self.pin_backward.on()
