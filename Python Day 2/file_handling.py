#create and write file

f= open("text.txt", "w")
f.write("Hello World")
f.close()
print("File Created ")

#read file

f=open ("text.txt", "r")
constant = f.read ()
print(constant)
f.close()   

#append file 
f=open("text.txt", "a")
f.write("\nWelcome to Python")
f.close()