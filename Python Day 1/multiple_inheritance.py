class Parent:
    def property(self):
        print("Dad own a house")

class Mother:
    def cooking(self):
        print("mother cooks good food")
    
class child(Parent, Mother):
    def bike(self):
        print("child own a bike")

s = child()
s.bike()
s.property()
s.cooking()