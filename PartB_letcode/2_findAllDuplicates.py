# =========== Find All Duplicate in an Array ===============
"""
    Given an integer nums of lenght n where all the integers of nums are in the range [1, n] and each integer appears
    once or twice, 
    returnan array of all the integers that appears twice.
    
    ---input = nums = [4,3,2,7,8,2,3,1]
    ---output [2,3]
"""


def findDuplicate(nums):
    n = len(nums)
    res = []
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] == nums[j] and nums[i] not in res:
                res.append(nums[i])
    return res

# ========= using hashsets ==========


def findDuplicate2(nums):

    res = set()
    seen = set()

    for i in nums:
        if i in seen:
            res.add(i)
        else:
            seen.add(i)
    return res


print(findDuplicate2([1, 2, 3, 2, 2, 2, 2, 2, 4, 4, 5, 6, 7, 7]))
