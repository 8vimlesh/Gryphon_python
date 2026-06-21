class GrandFather:
    def land(self):
        print("Grand Father own 2acr land")

class Parent(GrandFather):
    def property(self):
        print("Dad own a house")

    
class child(Parent):
    def bike(self):
        print("child own a bike")

s = child()
s.property()
s.land()