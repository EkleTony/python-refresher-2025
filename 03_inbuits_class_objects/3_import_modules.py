# Python Standard libraries and modules

"""
   ============= Python modules ============
   1. math module: using is import math
   2. import pi
   3. import random
   4. tabulate

"""
import math
from math import pi
import random as r
from tabulate import tabulate


print("============= math module ==========")

for i in range(5, 12):
    print(f"Square {i} == {math.pow(i, 2)}", end=" \t")
    print(f"Square root {i}  == {math.sqrt(i)}")


print("\n =========Area of circle ========")
radius = 4.823
print(f"Circumference is: {2 * pi * radius}")
print(f"Area: {pi * math.pow(radius, 2)}")


# Using Random
# return int from between two numbers
print("random value: ", r.randint(1, 20))
print(f"Random float: {round(r.random(), 4)}")  # returns any float
print(f"random_uniform: {r.uniform(2, 5)}")  # returns float between 2 and 5
# return a random seletced element from the non-empty seq
print(f"random_randrange {r.randrange(5, 25, 2)}")
# return a random element from athe non-empty sequence
print(f"random choice {r.choice([2, 3, 4, 5, 5])}")
mylist = [4, 5, 3, 4, 8, 9]
print(f"my list: {mylist}")
r.shuffle(mylist)  # shuffles the sequence x in place
print(mylist)
print("Samples: ", r.sample(range(1, 9), 6))

print("\n =========== Generate Random Numbers ===============")
n = 10
li = r.sample(range(1, 101), 30)
print(li)

print(f"\n ======== Random floats ====")
print([r.uniform(2, 9) for _ in range(20)])


print()
print(f"============ Print Tabulated data=============")

# sample data
data = [
    ["Product", "Price", "Stock"],
    ["Laptop", 667.4, 45],
    ["Mouse", 56, 23.90],
    ["Keyboard", 56.77, 89]
]

# creating a formulated table
print(tabulate(data, headers='firstrow', tablefmt="double_outline"))
