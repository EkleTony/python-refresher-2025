""" =======Leetcode 560---Subarray Sum Equals
q1: Given an array nums and integer k, return the number of subarrays whose sum equal k.
"""


def subArray(nums, k):
    n = len(nums)
    count = 0

    for i in range(n):
        cur_sum = 0
        for j in range(i, n):
            cur_sum += nums[j]
            if cur_sum == k:
                count += 1

    return count


nums = [1, 1, 1]
k = 2
print(f'SubArray Sum if {nums} and k = {k} is {subArray(nums, k)}')
