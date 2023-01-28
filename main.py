from car import Car

car = Car()
car.blink_led(times=5, delay=1)
car.forward(time=5)
car.turn_left(time=1)
car.backward(time=5)
car.turn_left(time=1, speed=50)
car.blink_led(times=10, delay=0.1)
