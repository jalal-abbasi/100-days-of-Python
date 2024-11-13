from car import Car
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
YRANGE = (-250, 270)
NUMOFCARS = 20


class CarManager:
    def __init__(self):
        self.car_list = []
        self.generate_cars()
        self.pace = STARTING_MOVE_DISTANCE

    def generate_cars(self):
        for _ in range(NUMOFCARS):
            car = Car(choice(COLORS))
            self.car_list.append(car)

    def move_cars(self):
        for car in self.car_list:
            car.backward(self.pace)
            if car.xcor() < -310:
                car.goto(310, randint(YRANGE[0], YRANGE[1]))

    def speed_up(self):
        self.pace += MOVE_INCREMENT








