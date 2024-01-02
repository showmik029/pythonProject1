"""
class Publication:
    def __init__(self,name):
        self.name=name
class Book(Publication):
    def __init__(self,name,author,page_count):
        super().__init__(name)
        self.author=author
        self.page_count=page_count
    def print_information(self):
        print(f"Publication: {self.name} Book Author: {self.author} Page Count: {self.page_count}")

class Magazine(Publication):
    def __init__(self,name,magazine_author):
        super().__init__(name)
        self.magazine_author = magazine_author
    def print_information(self):
        print(f"Publication: {self.name} Chef Editor: {self.magazine_author}")

p1=Magazine("Donald Duck","Aki Hyyppa")
p1.print_information()
b1=Book("Compartment No 6","Rosa Liksom",192)
b1.print_information()
"""
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

class ElectricCar(Car):
    def __init__(self,registration,maxspeed,battery_cap):
        super().__init__(registration,maxspeed)
        self.battery_cap=battery_cap
    def print_km(self):
        print(f"Electric car:{self.registration} goes {self.dt} km")

class Gasoline(Car):
    def __init__(self, registration, maxspeed, gas):
        super().__init__(registration, maxspeed)
        self.gas_cap = gas

    def print_km(self):
        print(f"Gasoline:{self.registration} goes {self.dt} km")

e=ElectricCar("ABC-15", 180, 52.5)
e.accelerate(60)
for i in range(1,4):
    e.drive(1)
    e.print_km()

g=Gasoline("ACD-123",165,32.3)
g.accelerate(70)
for i in range(1,4):
    g.drive(1)
    g.print_km()




