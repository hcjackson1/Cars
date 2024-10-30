class Car:
    def __init__(self, make, model, year, price):
        self.make = make.upper()
        self.model = model.upper()
        self.year = year
        self.price = price

    def __gt__(self, rhs):
        if self.make.upper() > rhs.make.upper():
            return False
        if self.make.upper() < rhs.make.upper():
            return True
        if self.model.upper() > rhs.model.upper():
            return False
        if self.model.upper() < rhs.model.upper():
            return True
        if self.year > rhs.year:
            return True
        if self.year < rhs.year:
            return False
        if self.price > rhs.price:
            return True
        else:
            return False
            

    def __lt__(self, rhs):
        if self > rhs:
            return False
        if self != rhs:
            return True
        else:
            return False
            

    def __eq__(self, rhs):
        if rhs == None:
            return False
        return self.make == rhs.make.upper() and self.model == rhs.model.upper() \
               and self.year == rhs.year

    def __str__(self):
        return f"Make: {self.make}, Model: {self.model}, Year: {self.year}, Price: ${self.price}"

'''
c = Car("Honda", "CRV", 2007, 8000)
c1 = Car("Honda", "CRV", 2007, 8000)
c2 = Car("dodge", "dart", 2015, 6000)
print(c1 < c2)
print(c2 > c1)
print(c1)
'''

