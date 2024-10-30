class CarInventoryNode:
    def __init__(self, car):
        self.car = car
        self.make = car.make
        self.model = car.model
        self.cars = [car]
        self.parent = None
        self.left = None
        self.right = None

    def get_make(self):
        return self.make

    def get_model(self):
        return self.model

    def get_parent(self):
        return self.parent

    def set_parent(self, parent):
        self.parent = parent

    def get_left(self):
        return self.left

    def set_left(self, left):
        self.left = left

    def get_right(self):
        return self.right

    def set_right(self, right):
        self.right = right

    def __str__(self):
        result = ""
        for car in self.cars:
            result += str(car) + "\n"
        return result
