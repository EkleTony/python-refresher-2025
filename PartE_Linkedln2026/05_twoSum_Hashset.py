""" 
    Leetcode 1: Two sum hashmap and sets..
    
    Q1: given an array of integers nums and an integer target return indices fo two nums such ahtat they add up 
    to target.
    
    e.g, nums =[2,3,4] target= 6
    ouptut [1,2]
    
"""


def twoSum(nums, target):
    # .. brute force O(n^2) and space O(1)
    n = len(nums)
    for i in range(n):
        for j in range(i, n):
            if nums[i] + nums[j] == target:
                return [i, j]


print("Two sum index--loop: ", twoSum([1, 2, 3, 4], 6))


# ========= Using HashMap======

def twoSumHashMap(nums, target):
    seen = {}  # using a hashmap or dic-- allow constant time insertion and lookup
    # e.g, [4,2,3,-5]... {4:0, 2:1, 3:2, -5:3}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]

        seen[num] = i


print("Two Sum with hashMap:", twoSumHashMap([1, 2, 3, 4, 5], 6))


def twoSum2(nums, target):
    # num = [2,3,4] , t=5
    seen = {}  # dictionary to store number → index

    for ind, num in enumerate(nums):  # loop through list with index and value
        # example mapping: value:index → 2:0, 3:1, 4:2, ...

        complement = target - num  # number needed to reach target-- e.g, for i, c=5-2=3

        if complement in seen:  # check if we've already seen the needed number
            # return indices of complement and current number
            # second iteration
            # 5-3 = 2, then if 2 in seen{2:0} yes, then return seen[2] i.e,0, and return ind=1
            # so we got [0,1] for 2 and for 3 =5
            return [seen[complement], ind]

        seen[num] = ind  # store current number and its index for future lookup
        # after 1st ieratiaon
        # seen = [2:0; ]


""" ============ Thress Sum==============="""


def three_sum(nums):
    nums.sort()
    result = []

    for i in range(len(nums) - 2):
        # Skip duplicate first elements
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                result.append([nums[i], nums[left], nums[right]])

                left += 1
                right -= 1

                # Skip duplicates
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

            elif total < 0:
                left += 1
            else:
                right -= 1

    return result


nums = [-1, 0, 1, 2, -1, -4]
print(three_sum(nums))
