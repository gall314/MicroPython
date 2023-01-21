# PWM

## What is PWM?

Pulse Width Modulation (PWM) is a technique used to control the power delivered to an electrical device, such as a motor, by rapidly turning the power on and off. This creates a series of pulses that can be used to control the speed, brightness, or other aspects of the device.

In MicroPython, the PWM class from the machine library can be used to create PWM signals to control the motors. The PWM class has several attributes and methods that can be used to configure and control the PWM signal.

Here are some of the most commonly used attributes and methods of the PWM class:

- **freq()**: This method is used to set the frequency of the PWM signal, which is the number of pulses per second.
- **duty()**: This attribute is used to set the duty cycle of the PWM signal, which is the percentage of time that the power is on during each pulse. A duty cycle of 100% means that the power is always on, and a duty cycle of 0% means that the power is always off.
- **deinit()**: This method is used to turn off the PWM signal and release the pin.

![PWM - Diagram](https://upload.wikimedia.org/wikipedia/commons/b/b8/Duty_Cycle_Examples.png)

```python
from machine import PWM, Pin

pwm = PWM(Pin(16))          # create a PWM object on a pin
pwm.duty_u16(32768)     # set duty to 50%

# reinitialise with a period of 200us, duty of 5us
pwm.init(freq=5000, duty_ns=5000)

pwm.duty_ns(3000)       # set pulse width to 3us

pwm.deinit()
```

So what it does - I can limit the speed of the motor or to be precise, the power of it

![PWM - out voltage](https://howtomechatronics.com/wp-content/uploads/2017/08/PWM-Working-Principle-Pulse-Width-Modulation-How-It-Works.png?ezimgfmt=ng:webp/ngcb2)

[Check Pico SDK examples](https://datasheets.raspberrypi.com/pico/raspberry-pi-pico-python-sdk.pdf)
