#  ============== LIST COMPREHENSION ============

# =========== What to look out for in a List-Comprehension =============
# 1.  returns a list
# 2. expresion i.e  i* 2 for i in iterable
# 3. iterable or something to loop over.! e.g
lst = [i*5 for i in [9, 4.5, 6, 7.8, 2.4, 7.9, 10]]
#print("simple example: ", lst)


# ===========Example with integers =============
num1 = [1, 2, 4]  # return a list of sum
nums = [i * 2 for i in num1]
print("list compreh..: ", nums)

# # Equivalent to for loop
# results = []
# for i in num1:
#     i = i*2
#     results.append(i)
# print("with for loop: ", results)


# ============= With String =================
strings = ["intro", "to", "list", "comps"]
results = []
for i in strings:
    i = i.upper()
    results.append(i)
#print("Ressults Strs: ", results)

#print("List comprh: ", [i.upper() for i in strings])



# ============== Function TimesFive ===========

def timesFive(num):
    return num * 5

results = []
for i in num1:
    i = timesFive(i)
    print("i = ", i)
    results.append(i)

# ======== Using a function in list comprehension ===========

result2 = [timesFive(i) for i in [6,7,8,9,12,34]]
print("Result with function: ", result2)
    
