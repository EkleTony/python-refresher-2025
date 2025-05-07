# Variable snd Basic Data types


# 1. Numbers
my_int = 10
my_float = 20.34
my_str = "this is a String bro"
my_bool = False


# Operators are used to perform operations on variables
print("=============== Operators ================")
print(my_int + my_float)
print(my_int * my_float)
print(my_int / my_float)
print("modulo", my_int % 2)

print("============= String operations=========")
another_str = "This is another string"
print(my_str + another_str)
print("nom" * 3)

# Logical and Comparison Operators
print("=============== Logical and Comparison operator========")
print(my_int == 10)
print(my_float != 20)
print(my_int > 20)
print(my_float < 20)

print(not (my_int > 5 and my_float < 30.0))


# Re-declaring variables
print("==== Variable re-declaring=======")
my_int = "abc"
print(my_int)
