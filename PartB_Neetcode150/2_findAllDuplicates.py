# =========== Find All Duplicate in an Array ===============
"""
    Given an integer nums of lenght n where all the integers of nums are in the range [1, n] and each integer appears
    once or twice, 
    returnan array of all the integers that appears twice.
    
    ---input = nums = [4,3,2,7,8,2,3,1]
    ---output [2,3]
"""


def findDuplicate1(nums):
    n = len(nums)
    res = []
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] == nums[j] and nums[i] not in res:
                res.append(nums[i])
    return res
# Time: o(n^2) and O(n^3) worst case!
# Space: O(d) where d is size of res

# ========= using hashsets ==========


def findDuplicate2(nums):

    res = set()
    seen = set()

    for i in nums:  # ======= single pase O(n)
        if i in seen:
            res.add(i)
        else:
            seen.add(i)
    return res


# Time: O(n) for loop and O(1) for set =
# Space: seen store all unique element O(n) and res == O(d)
# so space complexity is O(n)

def findDuplicate3(nums):
    res = set()

    for i in nums:
        m = abs(i)
        if nums[m-1] < 0:
            res.add(m)
        else:
            # mark this point seen before by multi by -1
            nums[m-1] *= -1
    return res


print(findDuplicate1([1, 2, 3, 2, 2, 2, 2, 2, 4, 4, 5, 6, 7, 7]))

print(findDuplicate2([1, 2, 3, 2, 2, 2, 2, 2, 4, 4, 5, 6, 7, 7]))

print(findDuplicate3([1, 2, 3, 2, 2, 2, 2, 2, 4, 4, 5, 6, 7, 7]))
