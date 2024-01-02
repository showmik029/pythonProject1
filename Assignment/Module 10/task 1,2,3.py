class Elevator:
    def __init__(self, bottom, top):
        self.top = top
        self.bottom = bottom
        self.current = bottom

    def go_to_floor(self, target):
        if target > self.top or target < self.bottom:
            print("INVALID FLOOR. PLEASE SOBER UP.")
            return
        while self.current != target:
            if target > self.current:
                self.floor_up()
            else:
                self.floor_down()

    def floor_up(self):
        self.current += 1
        print(f"Elevator floor: {self.current}")

    def floor_down(self):
        self.current -= 1
        print(f"Elevator floor: {self.current}")

class Building:
    def __init__(self, bottom, top, number):
        self.number = number
        self.elevators = [Elevator(bottom, top) for _ in range(number)]

    def run_elevator(self, elevator_num, target):
        if elevator_num > len(self.elevators) or elevator_num <= 0:
            print("Invalid elevator number.")
            return
        self.elevators[elevator_num - 1].go_to_floor(target)
        print(f"Elevator {elevator_num} reached floor {target}")

    def fire_alarm(self):
        for elevator in self.elevators:
            elevator.go_to_floor(elevator.bottom)
        print("Fire alarm activated. All elevators moved to the bottom floor.")


h = Elevator(0, 10)
h.go_to_floor(5)
h.go_to_floor(0)

B1 = Building(0, 10, 3)
B1.run_elevator(1, 5)
B1.run_elevator(2, 8)
B1.run_elevator(3, 2)

B2 = Building(0, 5, 2)
B2.run_elevator(1, 4)
B2.run_elevator(2, 1)

B1.fire_alarm()
