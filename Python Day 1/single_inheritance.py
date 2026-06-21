class Parent:
    def property(self):
        print("Dad own a house")
    
class child(Parent):
    def bike(self):
        print("child own a bike")

s = child()
s.bike()
s.property()