""" Kadane's Algorithm to Maximum Sum Subarray Problem

Given an integer array nums, find the contiguous subarray with the largest sum, and return that sum.

nums = [-2,1,-3,4,-1,2,1,-5,4]
answer = 6

Because the subarray [4,-1,2,1] has sum 6.

"""


def max_subarray1(num):
    cur_sum = num[0]
    max_sum = num[0]

    for i in range(1, len(num)):
        if cur_sum < 0:
            cur_sum = num[i]
        else:
            cur_sum += num[i]
        max_sum = max(max_sum, cur_sum)

    return max_sum


def max_subarray2(num):
    cur_sum = num[0]
    max_sum = num[0]

    for i in range(1, len(num)):
        # keep whichever gives a larger sum... i.e should we start a new subarray or continue prev
        cur_sum = max(num[i], cur_sum + num[i])
        max_sum = max(max_sum, cur_sum)

    return max_sum


num = [1, -3, 2, 1, -1]
print(f'Return Max SubArray in {num} is === {max_subarray1(num)} ')
print(f'Return Max SubArray in {num} is === {max_subarray2(num)} ')
