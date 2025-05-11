# ========= Functions ==============

import math

# 1...=== function to cal. the Square of list items


def Square(num):
    for i in num:
        area = i**2
        print(f"{i}*{i} == {area}cm^2")


print("======= Area ========")
Square([1.5, 2, 4, 6, 7, 12, 3.6, 7, 8, 14, 9])

print()
# Function with parameters and return
print("====Function to calculate RMSE=====")


def rmse(y1, y2):
    square_error = [(i-j)**2 for i, j in zip(y1, y2)]
    return math.sqrt(sum(square_error)/len(y1))


y1 = [1.1, 2.1, 3.3, 4.5, 5.2]
y2 = [1, 2, 3, 4, 5]
rmse = rmse(y1, y2)
print(f"rmse of {y1} and {y2} is {rmse}")

print()
# Functions with default value for an parameter


def greeting_func(greetings, name=None):
    print("Hello my people!")
    if name == None:
        name = input("What is your name? ")
    print(greetings, name)


greeting_func("Good Afternoon")


# ======Function with varable number of parameters
def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return "sum of ", args, "is = ", result


print(multi_add(3, 4, 5, 7, 8, 8, 3, 2))
