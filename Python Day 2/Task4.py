class BankAccount:
    __balance = 5000

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited {amount}. Balance: {self.__balance}")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance!")
        else:
            self.__balance -= amount
            print(f"Withdrawn {amount}. Balance: {self.__balance}")

    def get_balance(self):
        print(f"Balance: {self.__balance}")

# Account 1
acc1 = BankAccount()
acc1.deposit(2000)
acc1.withdraw(1000)

print("----------")

# Account 2
acc2 = BankAccount()
acc2.deposit(5000)
acc2.withdraw(10000)