""" ========== Two Sum with loop and pointers====
Q: Given a sorted array, find two numbers that sum to a target.

"""

""" ======== Sorted Array uses two poiners"""
arr1 = [1, 2, 3, 4, 5]
target1 = 5

# brute force


def twoSum_sorted(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i, n):
            if nums[i] + nums[j] == target:
                return [i, j]


""" =====wwhile unSorted Array uses Hashmap and enumerate, complement way """
arr2 = [3, 2, 4, 1]
target2 = 5
