class Parent:
    def property(self):
        print("Dad own a house")

class child1(Parent):
    def bike(self):
        print("child1 own a bike")

class child2(Parent):
    def car(self):
        print("child1 own a car")

class child3(Parent):
    def scooty(self):
        print("child1 own a scooty")

s = child3()
s.property()