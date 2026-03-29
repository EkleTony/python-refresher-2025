""" Two Sum=== Sorted array..

"""


def twoSum1(nums, target):
    # using two pointer in this case or brutefoces
    n = len(nums)
    for i in range(n):
        for j in range(i, n):
            if nums[i] + nums[j] == target:
                return [i, j]


arr = [1, 2, 3, 4, 5, 6]
#      0 1 2 3 4 5
target = 7


def twoSum2_pointer(nums, target):
    n = len(nums)
    left = 0
    right = n - 1

    while left < right:
        sum1 = nums[left] + nums[right]
        if sum1 == target:
            return [left, right]
        else:
            if sum1 < target:
                left += 1
            else:
                right -= 1


# ========== Unsorted array instead
def twoSum3_unsorted(nums, target):
    # using hash map
    # iterate with idex and value---- u
    # find the complement of target for each items and
    # check if the opposite exist in the hash.
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i


print(f'Two Sum is {twoSum1(arr, target)}')
print("=================")
print(f'Two Sum with Pointers is {twoSum2_pointer(arr, target)}')

print(f'Two Sum with Unsorted Array is {twoSum3_unsorted(arr, target)}')
