""" Continuous Subarray Sum - Leetcode 523 - Python

nums = [23, 2, 6, 4, 7] k = 6
output = true

[2,4] is a continuous subarray of size 2 whose elements sum up to 6.
ile x is mulple of k, if there exist an int n s.t x = n*k. 0 is always a multiple of k.
"""

""" ==== Method 1, brute forese===
--Idea--
Try every possible subarray of length at least 2, compute its sum, and check whether it is divisible by k.
"""


def bruteSubArray(nums, k):
    n = len(nums)
    for i in range(n):
        cur_sum = nums[i]
        for j in range(i+1, n):
            cur_sum += nums[j]

            if cur_sum % k == 0:
                return True
   #  return False


def optimalSubArray(nums, k):
    prefix_remainder = {0: -1}
    cur_sum = 0

    for i, num in enumerate(nums):
        cur_sum += num
        remainder = cur_sum % k
        if remainder not in prefix_remainder:
            prefix_remainder[remainder] = i
        elif i - prefix_remainder[remainder] >= 2:
            return True
    return False


nums = [23, 2, 4, 6, 7]
k = 6

print(f'Continuous Subarray of {nums} and {k}==== {bruteSubArray(nums, k)}')
print('=======')
print(f'Continuous Subarray of {nums} and {k}==== {optimalSubArray(nums, k)}')
