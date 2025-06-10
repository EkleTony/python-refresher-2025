# ========== REviewoing my codes ============

# 1. Find Closest Number to Zero - Leetcode 2239 - Arrays & Strings (Python)
nums = [-4, -2, 1, -1, 4, 8]
# nums = [5, -5]
# nums = [0, -1, 1]


def findClosestNumber(nums):
    closest = nums[0]
    result = []
    for num in nums:
        if (abs(num) < abs(closest) or abs(num) == abs(closest)) and num > closest:
            closest = num
    return closest


print(findClosestNumber(nums))
