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

