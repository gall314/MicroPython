# Step Motor and UNL2003 Driver

[How Stepper Motor Works](http://2.bp.blogspot.com/-wtsnTJc7DOM/T2I1YQ3N4GI/AAAAAAAAACk/u3m_u92O4ko/s1600/how_stepper_motor_works.gif)

![How it works](https://www.thegeekpub.com/wp-content/uploads/2021/02/How-Stepper-Motors-Work-0002-Rotation.png)

[Link](https://lastminuteengineers.com/28byj48-stepper-motor-arduino-tutorial/)

Gear Reduction Ratio
![Img](https://lastminuteengineers.b-cdn.net/wp-content/uploads/arduino/28BYJ48-Stepper-Motor-Gear-Ratio-Explanation.png)

According to the data sheet, when the 28BYJ-48 motor is operated in full step mode each step corresponds to a rotation of 11.25°. This means there are 32 steps per revolution (360°/11.25° = 32).
28byj48 stepper motor gear ratio explanation

Apart from this, the motor has 1/64 reduction gear set. (actually it is 1/63.68395 but for most purposes 1/64 is a good enough approximation)


The 28BYJ-48 typically consumes around 240mA.

Since the motor draws a lot of power, it is best to power it directly from an external 5V power supply rather than drawing that power from the microcontroller.

Note that the motor consumes power even in stand still state to maintain its position.



Don't reinvent the wheel
[MicroPython - UNL2003 Library](https://github.com/IDWizard/uln2003)
