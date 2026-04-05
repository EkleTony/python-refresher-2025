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
# O(n^2)


nums = [1, 1, 1]
k = 2
print(f'SubArray Sum if {nums} and k = {k} is {subArray(nums, k)}')


""" =========METHOD 2==========="""
# 1ntiuaiotn: instead of looking at each subarrays directly,
# let's think in terms of cumulative sums (prefix sums)


"""      | prefix_sum |  counts  |
         -------------|----------|
         |    0       |  1       |
         |            |          |
         |            |          |

"""


def subArraySum1(nums, k):
    count = 0
    prefix_sums = {0: 1}  # using dictionary
    cur_sum = 0

    for num in nums:
        cur_sum += num
        pref_sum = cur_sum - k

        # update the counts
        count += prefix_sums.get(pref_sum, 0)
        prefix_sums[cur_sum] = prefix_sums.get(cur_sum, 0) + 1
    return count


def bruteForce(nums, k):
    count = 0
    n = len(nums)

    for i in range(n):
        cur_sum = 0
        for j in range(i, n):
            cur_sum += nums[j]
            if cur_sum == k:
                count += 1
    return count


print(
    f"========== Brute force approach for {nums} k=2  == {bruteForce(nums, 2)}")

print(
    f"========== Using Prefix Sum and HashMap approach for {nums} k=2  == {subArraySum1(nums, 2)}")
