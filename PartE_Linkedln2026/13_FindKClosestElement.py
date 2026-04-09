"""
============ Find K Closest Elements - Leetcode 658 - Python ======

Q1: Given a sorted integer array arr, two integers k and x and return the k closest
integers to x in the array . 

the result should also be sorted in ascending ord.
    
 """

nums = [1, 2, 3, 4, 5]
x = 4
k = 3
# output = [1,2,3,4]


def find_closest_element1(nums, k, x):
    # sort by cloesest to x
    # break ties by smaller values and take first k, then sort
    # result = sorted(nums, key=lambda num: (abs(num - x), num))[:k]

    keys = (abs(nums-x), nums)
    return sorted(nums, key=keys)


# ======== Sliding window examples====
def sortedSquare(nums):
    res = []
    for x in nums:
        res.append(x**2)
    #res.sort()
    return sorted(res)
# time complexity === O(nlog n)--- becuase of sorting
# needs O(n) with pointers ===


print("======== Sliding Window================")
print(f'Squared of sorted array: {sortedSquare([1, -4, -2, 3, 5])}')
print()

# ========== Method 2: Using binary search


def find_closest_element(nums, k, x):
    left = 0
    right = len(nums) - k

    while left < right:
        mid = (left + right) // 2

        if x - nums[mid] > nums[mid + k] - x:
            left = mid + 1
        else:
            right = mid

    return nums[left: left + k]


print("========Method 2==========")
print(f'find the closest element: {find_closest_element(nums, k, x)}')
print("============ Method 1")
print(f'find the closest element: {find_closest_element(nums, k, x)}')
