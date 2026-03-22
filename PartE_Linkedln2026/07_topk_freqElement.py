"""---------Leetcode347----

    Q1: Given an integer array nums and an integer k, return the k most freq.
     element. You may return the answer in any order
    """

from collections import Counter
nums = [1, 1, 1, 2, 2, 3, 4, 4, 4, 5, 6]
k = 2

# output = [1,2,4]


def duplicateValue(nums):
    seen = set()
    res = set()
    for i in nums:
        if i in seen:
            res.add(i)
        else:
            seen.add(i)
    return res

# That soln above is actully for duplicate not freq K


""" Using Counter from collections..."""


def topKfreq2(nums, k):
    count = Counter(nums)   # {1:3, 2:2, 3:1, 4:3, 5:1, 6:1}
    mostCommon = count.most_common(k)  # {1:3, }
    ans = [num for num, freq in mostCommon]
    return ans


print("Return duplicate: ", duplicateValue(nums))
print("Most Freq k elements: ", topKfreq2(nums, k))
