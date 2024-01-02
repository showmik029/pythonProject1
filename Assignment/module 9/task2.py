class Car:
    def __init__(self, registration, maxspeed,currentspeed=0,dt=0):
        self.registration = registration
        self.maxspeed = maxspeed
        self.currentspeed = currentspeed
        self.dt =dt

    def display(self):
        print(f'Registration: {self.registration}\nMax Speed: {self.maxspeed} km/h\n'
              f'Current Speed: {self.currentspeed} km/h\nTravelled Distance: {self.dt} km\n')

    def accelerate(self, speed_change):
        self.currentspeed += speed_change
        if self.currentspeed > self.maxspeed:
            self.currentspeed = self.maxspeed
        elif self.currentspeed < 0:
             self.currentspeed = 0

new_car = Car("ABC-123", 142)

new_car.accelerate(30)
new_car.accelerate(70)

print(f'Current Speed after acceleration: {new_car.currentspeed} km/h')
new_car.accelerate(-200)

print(f'Final Speed after emergency brake: {new_car.currentspeed} km/h')
