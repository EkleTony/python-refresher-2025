""" 
    Leetcode 217--Contains Duplicate
    
    Q1: Given an integer array nums.. return true if any value appears at least twice in the array and 
    return false if every element is distinct
    
    e.g, input nums = [1,2,3,1]
    oupput== true
"""


def findDuplicate(nums):

    seen = set()
    result = set()

    for i in nums:
        if i in seen:
            result.add(i)
        else:
            seen.add(i)
    return result


print("duplicate found is : ", findDuplicate([1, 2, 3, 1]))


def containDuplicate(nums):
    seen = set()
    for i in nums:
        if i in seen:
            return True
        else:
            seen.add(i)
    return False


print("Return True for duplicate: ", containDuplicate([1, 2, 3, 4, 1]))


def bruteForce(nums):
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] == nums[j]:
                return True

    return False


def usingSort(nums):
    # O(nlog n)
    # nums.sort()

    # for i in range(len(nums)):
    #     if nums[i] == nums[i-1]:
    #         return True
    # return False
    seen = set()
    for i in nums:
        if i in seen:
            return True
        else:
            seen.add(i)  # putting it into the hash set
    return False


print("BruteFoces Duplicate found: ", bruteForce([1, 2, 3, 4, 1]))
print("Using sorting and loop:", usingSort([1, 2, 3, 4, 1]))
