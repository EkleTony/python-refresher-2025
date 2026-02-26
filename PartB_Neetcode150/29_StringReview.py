# ========= Python Strings =======
"""  ========= Pythons Strings
    ---IN short a python string is a sequuence of characters enclosed in "" or '' or triples
    ---and they're immutables.
    
"""
# e.g
s = "Hello, my name is Tony"
lst = ["h", "e", "l", "l", "o"]
age = 90

print("".join(lst))
print(str(age))
print("abc"*3)
print("Anthony " + "Ekle")

# ====== 1. Concatenation in loop is inefficient=====
s = ""
# for i in range(1000):
#     s += "a"

chars = ["a"] * 10
s = "".join(chars)  # single operations
print(s)
name = "Anthony"
print(name[::-1])
print(name.lower())
print(name.title())


# ========= Checking string properties
""" 
1. s.isalnum()--- checking for alphanumerics
2. s.isalpha() --- check if all characters are alphabetic
3. s.isdigit() --- check if all character are digit
4. s.isspace() --- whitespace
5. s.islower() --- check for lowercase
6. s.isupper() --- if uppercase

#========= Splitting and joining ====
7. s.split(sep, [maxsplit])
e.g. 
"""
sp = "Leet, Code, python"
print("=========== Splitting and joining =======")
split = sp.split(",")
print(split)
print(" --".join(split))

# ==== Leetcode Examples
# Check if a string is palindrome---leetcode #125
print("========== Ispalindrome============ \n")
palin = "aba1"

from collections import Counter
def isPalindrome(st):
    lc = [i.lower() for i in st if i.isalnum()]
    s = "".join(lc)
    return s == s[::-1]



print(isPalindrome(palin))
