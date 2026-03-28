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
    # [1,2,3,4] t =4
    #  l     r -- if s= num[l] + num[r] == t, return else if s<t, increase l else reduce r
    left = 0
    right = len(nums)-1

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

arr2 = [1, 3, 2, 4, 7, 5, 1, 6]
#       0  1  2  3  4  5  6  7
target2 = 6
print(f'Unsorted array: {twoSum_sorted(arr2, target2)}')
print("======= Building Method for unsorted array using hash map.. ")


def twoSum_unsorted(nums, target):
    # build a hashmap or dict
    # enumerate and find complement
    # check if the compllement + any eleemnt == target
    # return that value whose complent and the num (incie)
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]

        # else update
        seen[num] = i


print(f'Unsorted array--Failed Solution: {twoSum_sorted(arr2, target2)}')

print(f'Unsorted array--Better Solution: {twoSum_unsorted(arr2, target2)}')




""" ===== Next on two pointers

2. 3Sum (VERY important) (sort + fix one element
two pointers inside)

3. 3. Container With Most WaterProblem (Max area between two vertical lines
Pattern
start wide (edges)
move the smaller height inward

 4. Remove Duplicates from Sorted Array
 
 
 5. 5. Valid Palindrome
Problem

Check if string is palindrome (ignore non-alphanumeric)

Pattern
left/right pointers
skip invalid chars


"""
