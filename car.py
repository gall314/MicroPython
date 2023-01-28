from motor import Motor
from machine import Pin
import utime
import config


class Car:
    def __init__(self):
        self.motor_left = Motor(config.PIN_LEFT_FORWARD, config.PIN_LEFT_BACKWARD, config.PIN_LEFT_SPEED)
        self.motor_right = Motor(config.PIN_RIGHT_FORWARD, config.PIN_RIGHT_BACKWARD, config.PIN_RIGHT_SPEED)
        self.led_left = Pin(config.PIN_LED_LEFT, Pin.OUT)
        self.led_right = Pin(config.PIN_LED_RIGHT, Pin.OUT)
        self.led_onboard = Pin(config.PIN_LED_ONBOARD, Pin.OUT)

    def forward(self, speed=100, time=0):
        self.motor_left.speed(speed)
        self.motor_right.speed(speed)
        self.delay_stop(time)

    def backward(self, speed=100, time=0):
        self.motor_left.speed(-speed)
        self.motor_right.speed(-speed)

    def turn_left(self, speed=100, time=0):
        self.motor_left.speed(speed)
        self.motor_right.speed(-speed)

    def turn_right(self, speed=100, time=0):
        self.motor_left.speed(-speed)
        self.motor_right.speed(speed)

    def blink_led(self, times=5, delay=1):
        for x in range(2 * times):
            self.led_onboard.value((x+1) % 2)
            utime.sleep(delay)

    def delay_stop(self, time):
        if time > 0:
            utime.sleep(time)
            self.stop()

    def stop(self):
        self.motor_left.stop()
        self.motor_right.stop()
