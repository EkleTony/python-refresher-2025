""" 4Sum---Leetcode 18

Q: given 4 uniqu quafrulets  num[a] + num[b] + num[c] + num[d] == target return [a,b,c,d]
"""


nums = [1, 0, -1, 0, -2, 2]
target = 0

""" Generalizing for K-sum, will give us recursive function....!"""


def fourSum(nums):
    nums.sort()

    n = len(nums)
    result = []

    for i in range(n):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        for j in range(i+1, n):
            if j > i+1 and nums[j] == nums[j-1]:
                continue

            # now using two pointers
            l = j + 1
            r = n - 1

            while l < r:
                sum4 = nums[i] + nums[j] + nums[l] + nums[r]

                if sum4 == 0:
                    result.append([nums[i], nums[j], nums[l], nums[r]])
                    l += 1
                    r -= 1

                    # checking for duplicattes
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1

                else:
                    if sum4 < 0:
                        l += 1
                    else:
                        r -= 1
    return result


print("========== 4Sum ==========")
print(f'4Sum of {nums} is {fourSum(nums)}')
