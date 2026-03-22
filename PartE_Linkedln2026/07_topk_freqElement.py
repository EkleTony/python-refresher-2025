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


def topFreq3(nums, k):
    count = {}
    freq = [[] for i in range(len(nums) + 1)]

    for n in nums:
        count[n] = 1 + count.get(n, 0)
    for n, c in count.items():
        freq[c].append(n)

    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res


print("Return duplicate: ", duplicateValue(nums))
print("Most Freq k elements: ", topKfreq2(nums, k))


def twoSumReview(nums, target):

    n = len(nums)
    for i in range(n):
        for j in range(i, n):
            if nums[i] + nums[j] == target:
                return [i, j]


def twosum2(nums, target):
    # using a hashmap approach

    seen = {}
    for i, num in enumerate(nums):  # mapping, {1:0, 2:1, 3:2, 4:3...}
        complement = target - num  # for i=0, i.e 1, 5-1= 4
        if complement in seen:  # is 4 in seen? no or yes,
            return [seen[complement], i]  # the value and idex
        seen[num] = i  # if com =4, and 3 seen {4:0, 3:1, 2:2 }


nums = [1, 2, 3, 4]
target = 5
print(f'Two Sum of {nums} and {target} is {twoSumReview(nums, target)}')
print(f'Two Sum method2 is {twosum2(nums, target)}')
