students_age = [23, 34, 34, 56, 12, 30.5, "Yazmin"]
print(students_age)
print(students_age[3])

# Slicing in lists.
my_list = ["p", "y", "t", "h", "o", "n"]
print(my_list[-4:-1])
print(my_list[:4])
print(my_list[1:-2])

# Appending
numbers = [1, 2, 3, 4, 5, 6]
numbers.append(9)
print(numbers)

my_tuple = (2, 3, 3, 4, 5, 87)
print(my_tuple[2])
print(my_tuple.count(3))


stack = []
stack.append(3)
stack.append(5)
stack.append(6)
stack.append(7)
stack.append(90)

print(stack)
print(stack.pop())