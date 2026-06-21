class Person:
    __name = "rahul" #private variable

    def get_name(self):
        print(self.__name) #getter method


p = Person()
p.get_name()