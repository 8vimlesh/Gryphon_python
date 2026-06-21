a= 10
b= 0

try: 
    print(a/b)
except ZeroDivisionError:
    print("Cannot divide by zero")

try:
    num = int(input("abc"))

except ValueError:
    print("Invalid input")

    