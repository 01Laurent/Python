# storing numbers
FavNum = 50
print(f"My fav number is {FavNum}")

# storing strings
hello = "Hello, Laurent"
print(hello)

# boolean variables
IsPythonFun = True
print(f"Is python fun? {IsPythonFun}")

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