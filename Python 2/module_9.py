#task1

class Car:
    def __init__(self,registration,maxspeed,currentspeed=0,dt=0):
        self.registration=registration
        self.maxspeed=maxspeed
        self.currentspeed=currentspeed
        self.dt=dt
    def display(self):
        print(f'Registration:{self.registration}\nMaxSpeed:{self.maxspeed}\nCurrentSpeed:{self.currentspeed}\nDT:{self.dt} km')

    def accelerate(self, acceleration):
        self.currentspeed += acceleration
        if self.currentspeed > self.maxspeed:
            self.currentspeed = self.maxspeed
        elif self.currentspeed < 0:
            self.currentspeed = 0
    def drive(self,hours):
        self.hours=hours
        self.dt=self.dt+(self.hours*self.currentspeed)

#MODULE 10 TASK 4
class Race:
    def __init__(self,name,total_distance,carlst):
        self.carlst = carlst
        self.name=name
        self.total_distance=total_distance
        self.laps=0

    def  hour_passes(self):
        for i in self.carlst:
            i.accelerate(random.randint(-10, 15))
            i.drive(count)
    def race_finished(self):
        for car in self.carlst:
            if car.dt>self.total_distance:
                return True

    def print_status(self):
        status = ""
        for i in carlst:
            status += f"Name:{i.registration} Distance travelled: {i.dt} speed: {i.currentspeed}\n"
        return status



import random

carlst=[]
for i in range(1,11):
    ms=random.randrange(100,200,1)
    carlst.append(Car("ABC" + str(i), ms))
r=Race("Grand Demolition",8000,carlst)
count=0
winner=(Car("x",0))
while not r.race_finished():
    r.hour_passes()
    count+=1
    if count%10==0:
        print(r.print_status())

print(f"winner: \n{r.print_status()}")

for car in carlst:
    if car.dt > winner.dt:
        winner = car
print(f"\nThe race is over! The winner is {winner.registration} with a total distance of {winner.dt} km.")






