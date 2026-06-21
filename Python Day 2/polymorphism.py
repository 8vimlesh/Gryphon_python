#overloading - Here, one method handles different numbers of arguments, achieving overloading-like behavior.

class Women:
    def women(self):
        print("someones mom")

class Employee(Women):
    def women(self):
        print("she is a women")

class Driver:
    def women(self):
        print("she is driving a car")

s = Women()
s.women()


#overriding - The Dog class overrides the sound() method of the Animal class.

class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

dog = Dog()
dog.sound()