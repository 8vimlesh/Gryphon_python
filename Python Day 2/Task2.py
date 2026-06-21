class student:
    __marks = 0

    def set_marks(self, marks):
        self.__marks = marks

    def add_marks(self, marks):
        self.__marks += marks

    def get_marks(self):
        print(self.__marks)
    
s = student()
s.set_marks(85)         
s.add_marks(10)
s.get_marks()


