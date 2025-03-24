print("i love pizza")
#strings
first_name = "dama"
food = "chicken"
print(f" hello {first_name}")
print(f"I love {food}")
#intergers
age = 25
distance = 60
print(f"i'm {age}years old")
#float
price = 100.77
print(f"the cooking oil is{price}shillings")
#boolean
is_student = True
print(f"are you a student? {is_student}")
if is_student:
    print("you're a student")
else:
    print("you're NOT a student")
    
    #functions
def happy_birthday(name, age):
    print(f"happy birthday to {name}")
    print(f"how old are you now,{age} years old")
    print(f"happy birthday to you")

happy_birthday("dama", 22)
happy_birthday("mel", 20)
#return
def add(x, y):
    z = x+y
    return z

def substract(x, y):
    z = x-y
    return z

def multiply(x, y):
    z = x*y
    return z

def divide(x, y):
    z = x/y
    return z

print(add(1, 3))
print(substract(8, 6))
print(divide(9, 3))
print(multiply(4, 3))

#if...else statements

age = int(input("Enter your age: "))

if age >= 18:
    print("you're now signed up!")
    
elif age<=0:
    print("you have'nt neen born yet!")
    
else:
    print("you must be 18+ to sign up!")
    
#user input
name = input("What is your name?: ")  

#arithmetic operations
import math

pi = 3.14
x = 1
y = 2
z = 3
print(max(x,y,z))

pi = 3.14
x = 1
y = 2
z = 3
print(max(x,y,z))
print(min(x,y,z))
    

#slicing and indexing
#START,STOP,STEP
name = "Dama Kimeli"
first_name = name[3]
print(first_name)

#stop
name = "fana tic"
first_name = name[0:1]
print(first_name)
    #output...skip by 1..fn
    
#step
name = "dama kimeli"
f_name = name[0:10:3]
#output...dail

#slicing
name = "dama.kimeli.com"
slice = slice(4,-3)
#output...kimeli

#logical operators
temp = int(input("What is the temperature today?"))




while len(name) == 0:
    print("what is your name?")



