from collections import Counter
import random

obj_list = ["A", "B", "C", "C"]

# dct = {}

# this can be replace with counters
counter = Counter()
# for obj in obj_list:
#     dct[obj] = 0

for _ in range(100):
    recv_obj = random.choice(obj_list)
    counter[recv_obj] += 1
print(counter)


# ======= Examplle two
nums = [1, 1, 1, 2, 2, 3]
k = 2


def topK(nums, k):
    count = Counter(nums)
    topk_mostcommon = count.most_common(k)  # O(nlogn)
    # print(count)
    # print(topk_mostcommon)
    return [v for k, v in topk_mostcommon]


# print(topK(nums, k))


# ========= More examples from GeekforGeeks =========

a = [12, 3, 4, 5, 5, 11, 12, 6, 7, 5, 6, 8, 4]
x = Counter(a)


## =======Keys, and Values===
print(x)
for i in x.keys():
    print(f"{i} : {x[i]} ")
print(list(x.keys()))
print(list(x.values()))
