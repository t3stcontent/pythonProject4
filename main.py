import math


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print(f"{self.name} перестав існувати")

    def show_info(self):
        print(f"Name = {self.name}\tAge = {self.age}")

class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def square(self):
        print(f"Square = {self.w * self.h}")

    def per(self):
        print(f"per = {(self.w + self.h) * 2}")

class Circle:
    def __init__(self, r):
        self.radius = r

    def per(self):
        return round(2 * math.pi * self.radius, 2)

    def area(self):
        return round(math.pi * self.radius * self.radius, 2)



kolo1 = Circle(5)
print(kolo1.area())
print(kolo1.per())

r1 = Rectangle(10, 5)
r1.square()
r1.per()

round(123.12345,2)
