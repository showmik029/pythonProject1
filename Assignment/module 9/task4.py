class Car:
    def __init__(self, registration, maxspeed, currentspeed=0, dt=0):
        self.registration = registration
        self.maxspeed = maxspeed
        self.currentspeed = currentspeed
        self.dt = dt

    def display(self):
        print(f'Registration: {self.registration}\nMaxSpeed: {self.maxspeed} km/h\n'
              f'CurrentSpeed: {self.currentspeed} km/h\nDT: {self.dt} km')

    def accelerate(self, acceleration):
        self.currentspeed += acceleration
        if self.currentspeed > self.maxspeed:
            self.currentspeed = self.maxspeed
        elif self.currentspeed < 0:
            self.currentspeed = 0

    def drive(self, hours):
        self.dt += hours * self.currentspeed

# Car race simulation
import random

carlst = []
for i in range(1, 11):
    ms = random.randrange(100, 200, 1)
    carlst.append(Car("ABC-" + str(i), ms))

winner = Car("x", 0)
while True:
    for car in carlst:
        car.accelerate(random.randint(-10, 15))
        car.drive(1)
        if car.dt > winner.dt:
            winner = car
    if winner.dt >= 10000:
        break

print("{:<10} {:<15} {:<15} {:<15}".format("Registration", "Max Speed (km/h)", "Current Speed (km/h)", "Travelled Distance (km)"))
for car in carlst:
    print("{:<15} {:<20} {:<20} {:<25}".format(car.registration, car.maxspeed, car.currentspeed, car.dt))

print(f"\nWinner Car: {winner.registration} with a distance of {winner.dt} km.")
