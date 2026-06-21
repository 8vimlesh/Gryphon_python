#Abstraction means showing "what an object does" rather than "how it does it."

from abc import ABC, abstractmethod

class Payment (ABC):
    @abstractmethod
    def pay(self):
        pass
    def pay(self):
        pass

class Gpay (Payment):
    def pay(self): 
        print("Paying with Gpay")

class cash(Payment):
    def pay(self):
        print("Paying with cash")

gpay = Gpay()
gpay.pay()
cash = cash()
cash.pay()
