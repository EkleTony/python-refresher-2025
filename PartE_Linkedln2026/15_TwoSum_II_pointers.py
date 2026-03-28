""" ========== Two Sum with loop and pointers====
Q: Given a sorted array, find two numbers that sum to a target.

"""

""" ======== Sorted Array uses two poiners"""
arr1 = [1, 2, 3, 4, 5]
target1 = 5


def twoSum_sorted(nums, target):
    # ===========brute-force==========
    # n = len(nums)
    # for i in range(n):
    #     for j in range(i, n):
    #         if nums[i] + nums[j] == target:
    #             return [i, j]

    # ========= Using two pointers ==========
    left = 0
    right = len(nums) - 1

    while left < right:
        sum1 = nums[left] + nums[right]
        if sum1 == target:
            return [left, right]
        else:
            if sum1 < target:
                left += 1
            else:
                right -= 1


print(
    f'Using Sorted Array {arr1} and  target {target1} Brute-Force: {twoSum_sorted(arr1, target1)}')


# ========now using Two pointers=========


""" =====wwhile unSorted Array uses Hashmap and enumerate, complement way """
arr2 = [3, 2, 4, 1]
target2 = 5
