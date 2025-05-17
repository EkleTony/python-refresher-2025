#  --- ============= Given an Array nums, return true if any value appears at least twice in the array,
# and return false if every element is distinct


#
#
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


# output [2, 3
