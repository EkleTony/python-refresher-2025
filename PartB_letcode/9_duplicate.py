#  --- ============= Given an Array nums, return true if any value appears at least twice in the array,
# and return false if every element is distinct


#
#
from collections import defaultdict
from collections import Counter
input = nums = [4, 3, 2, 7, 8, 3, 1]

count = Counter(nums)
# duplicates = [strTrue for k, v in count.items() if v > 1] # O(n)


def findDuplicate(nums):
    count = Counter(nums)
    print(count)
    for k, v in count.items():

        if v >= 1:
            return True
        else:
            return False


x = findDuplicate(nums)
print(x)

# ========== DefualtDict

d = defaultdict(list)
d["names"].append("Anthony")
d['age'].append(29)
d['school'].append("TTU")
print(f"defualt dict: {d.keys()}")


# ========= default_factory arg of int

dic = defaultdict(int)
nums = [1, 2, 1, 3, 4, 5, 2, 1, 2, 3, 6, 7, 8, 2, 3, 2, 1, 2]

for i in nums:
    dic[i] += 1
frq = [k for k, v in dic.items() if v == max(dic.values())]
print(f"Num Freq: {frq[0]}")

# O(n) i.e counting and list comprehension O(k)
# Space is O(k)
# output [2, 3
