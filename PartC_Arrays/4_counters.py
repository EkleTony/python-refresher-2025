# =========== Python Counters ===============

from collections import Counter
import random


# 1. list of objects
lst = ["A", "B", "C", "D", "E", "A"]

dct = {}  # using a dictionary

for obj in lst:
    dct[obj] = 0

for _ in range(100):
    recv_obj = random.choice(lst)
    dct[recv_obj] += 1

print(dct)


# ======================
# find the item wiht highest frequency
nums = [2, 3, 4, 5, 6, 2, 3, 5, 6, 5, 2, 2]
count = Counter(nums)
x = max(count.values())

for key in count:
    print(f"Item {key} has the frequency {count[key]}")
print(f"maximum freq item is: {[k for k, v in count.items() if v == x]}")
print(f"max freq: {count.most_common(3)}")


# ========== Strings =========

string = "Hi there I am sample text. I am just sample repeat what i want to say there hi you are gine text right, just asking, thanks"
#print(string)
# spliting and lower case
list_string = string.lower().split(" ")
#print(list_string)

str_count = Counter(list_string)
print(str_count)

print(f"lenght is {len(str_count)}")

# most common 
print(str_count.most_common(4))
