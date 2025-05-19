# ============ Two Sum =================

"""Question:
    1. Given an array of integer return indices of the two numbers such that they add up to a specific target
        """

nums = [2, 7, 11, 15]
target = 9  # output= [0,1], i.e nums[0] + nums[1] = 9,

# Using brute force
print("\n=========== Using Brute Force= =============")


def twoSum1(nums, target):
    # res = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if nums[i] + nums[j] == target:
                return [[nums[i], nums[j]], [i, j]]
    # return res
# Time = O(n^2) and space = O(n)


print(twoSum1(nums, target))

print("\n============  Using Two Pointers ==============")


def twoSum2(nums, target):
    nums.sort()
    n = len(nums)
    l = 0
    r = n - 1

    while l < r:
        summ = nums[l] + nums[r]
        if summ == target:
            return [[nums[l], nums[r]], [l, r]]
        elif summ < target:
            l += 1
        else:
            r -= 1
  