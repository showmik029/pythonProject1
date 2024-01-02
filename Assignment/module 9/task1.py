class Car:
    def __init__(self, registration, maxspeed,currentspeed = 0,dt = 0):
        self.registration = registration
        self.maxspeed = maxspeed
        self.currentspeed=currentspeed
        self.dt=dt

    def display(self):
        print(f'Registration: {self.registration}\nMax Speed: {self.maxspeed} km/h\n'
              f'Current Speed: {self.currentspeed} km/h\nTravelled Distance: {self.dt} km\n')

    def accelerate(self, acceleration):
        self.currentspeed += acceleration
        if self.currentspeed > self.maxspeed:
            self.currentspeed = self.maxspeed
        elif self.currentspeed < 0:
            self.currentspeed = 0

    def drive(self, hours):
        self.dt += hours * self.currentspeed

new_car = Car("ABC-123", 142)
new_car.display()

