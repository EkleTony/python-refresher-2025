# =============== Using python inbuilt-in functions ================
mystr = "Hope you're having a great weekend, dude"
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 01 len() functions
print(f"length of str: {len(mystr)}")
print(f"length of my list: {len(mylist)}")

print()
print("====Min and Max function ======")
# min() and max() function
print(f"min: ", min(mylist))
print(f"max: {max(mylist)}")


# str(), int(), float() will return a data type verstion  of the values
print()
print("==== data type conversion====")
prefix = "result "
age = 26
print(f"prefix + age =  {prefix + str(age)}")


# the range() function
print()
print("===== Range() function =======")
for i in range(5, 10):
    print(f"square of {i} =  {i**2}")

print()
print(" ===== Range with interval")
for i in range(5, 10, 2):
    print(f"square {i} = {i**2}")


# The priint function itself is pretty flexible-- you can embed variables directly
# this we have been doing
name = "Anthony"
age = 29
print(
    f"Hello {name} you're {age} years old! Welcome to personal development world!")
