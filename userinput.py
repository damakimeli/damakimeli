import math
pi = -3.14
print(math.sqrt(900))

pi = 3.14
x = 1
y = 2
z = 3
print(max(x,y,z))
print(min(x,y,z))

#slicing\indexing
name = "Dama Kimeli"
first_name = name[3]
print(first_name)

#logical operators
temp = int(input("What is the temperature today?"))
if temp >= 0 and temp <= 30:
    print("The temperature is great today!")
    print("What a lovely day")
    
elif temp < 0 or temp > 30:
    print("temerature is bad today. Stay inside!")
    
    #while loop
while len(name) == 0:
    name = input("What is yor name:")
    
while len(name) == 0:
    print("what is your name?")
    
while len(name) == 0:
    name = input("What is yor name:")
    
print("Hello" +name)
    
    #for loop
    
for i in range(10):
    print(i)

    
    
    
    