# storing numbers
FavNum = 50
print(f"My fav number is {FavNum}")

# storing strings
hello = "Hello, Laurent"
print(hello)

# boolean variables
IsPythonFun = True
IsPythonBoring = False
print(f"Is python fun? {IsPythonFun}")
print(f"Is python boring? {IsPythonBoring}")

# control flow: IF, ELIF, ELSE
temperature = 15
if temperature > 25:
    print("Its hot outside! Keep it simple!")
elif temperature >= 15:
    print("Its warm! Maybe get a light Jacket")
else:
    print("its freezing! Keep warm and have your coffee with you!")

# LOOPS (FOR AND WHILE)
# for loops are used when you know the number of iterations
for i in range(5):
    print(f"This is a For loop iteration {i}")

# while loop
countdown = 5
while countdown > 0:
    print(f"Countdown {countdown}")
    countdown -= 1
print("Blast off!")

# Defining functions
def greet(name):
    return f"Hello, {name}"
#apply the function
print(greet("Laurent"))
print(greet("Annah"))


# ELSE IF ELIF
feast = 100
if feast > 90:
    print("The meal is delicious.")
elif feast >= 50:
    print("The meal is Yummy.")
else:
    print("The meal is nice.")

# LOOPS
for i in range(7):
    print(f"The door bell rings twice {i}")

countDown = 4
while countDown > 0:
    print(f"The countdown is {countDown}")
    countDown -= 1
print("The count down is over!!!")

def hello(someone):
    return f"Good Evening, {someone}!"
#application of the function
print(hello("Laurent"))
print(hello("Yazmin"))

#lists and dictionaries
# A list can be ordered and indexed.
# Dictionaries use key value pairs.
fruitsList = ["apple", "Mango", "Melon"]
fruitsTuple = ("cherry", "plums", "avocado")
print(fruitsList)
print(fruitsTuple)

#Dictionaries
contacts = {
    "Yazmin": "9876540",
    "Laurent": "987654",
    "Bob": "345678"
}
print(f"This contact belongs to Yazmin: {contacts["Yazmin"]}")

#modules
import math
result = math.sqrt(64)
print(f"The square root of 64 is : {result}")

#Custom
import practice
print(practice.hello("Yazmin"))