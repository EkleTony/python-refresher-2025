# ======== Arrays=========
# Single Non-repearing element in an array----leetcode 136
import math
arr = [2, 3, 4, 2, 9, 3, 4, 5, 5]


def singleNum(nums):
    a = 0

    for i in nums:
        a ^= i

    return a


print(singleNum(arr))


# === number closest to zeor
def minMax(arr):
    minNum = arr[0]
    maxNum = arr[0]
    for x in arr:
        if x <= minNum:
            minMax = x
    for y in arr:
        if y >= maxNum:
            maxNum = y
    return [minMax,  maxNum]


print(f"Min and max: {arr} is {minMax(arr)}")


def findMin(nums):
    res = nums[0]
    l = 0
    r = len(nums) - 1

    while l <= r:
        if nums[l] < nums[r]:
            res = min(res, nums[l])
            break
        m = (l + r)//2
        res = min(res, nums[m])
        if nums[m] >= nums[l]:
            l = m+1
        else:
            r = m - 1
    return res


print("==== unsorted array===!")
print(f"Min. number: {arr} is {findMin([2,5,1,6,7])}")


def minStartValue(nums):
    runningSum = 0
    minSum = 0

    for num in nums:
        runningSum += num
        minSum = min(minSum, runningSum)

    return -minSum + 1 if minSum < 1 else 1


print("\n======Summing=====\n")
num2 = [-2, -5, 6, -3]
print(sum(num2))
print(f"min sum of {num2} is =  {minStartValue(num2)}")


# ========== Mnimum Bit Flips to convert numbers==========
""" A bit flip of a number x is choosing a bit in a the binary representation of x and flipping it
from either 0 to 1 or 1 to 0....!

Question: Given two integers starts and goal, return the min number of bit flips
to convert start to goal.."""

# 10 = 1010---> 3 flips
# 7 == 0111


def minBitFlips(start, goal):
    flips = 0

    while goal or start:
        gbit = goal & 1
        sbit = start & 1
        if gbit != sbit:
            flips += 1
        goal >>= 1
        start >>= 1
    return minBitFlips


print(f"flip bits: start=1010 & goal = 0111 = {minBitFlips(1010, 111)}")

# ====Find closest to zero...


def closeZero(numb):
    closest = numb[0]
    for x in numb:
        if abs(x) < abs(closest):
            closest = x
    if closest < 0 & abs(closest) in numb:
        return abs(closest)
    else:
        return closest


arr3 = [-4, -2, 1, 4, 8]
print(f"Closest Number {arr3} = {closeZero(arr3)}")

# ========== merge String alternatively
word1 = "abc"
word2 = "pqr"  # output= apbqcr


def mergeWord(word1, word2):
    A = len(word1)
    B = len(word2)
    a, b = 0, 0
    word = 1
    s = []

    while a < A and b < B:
        if word == 1:
            s.append(word1[a])
            a += 1
            word = 2
        else:
            s.append(word2[b])
            b += 1
            word = 1
    while a < A:
        s.append(word1[a])
        a += 1
    while b < B:
        s.append(word2[b])
        b += 1
    return ''.join(s)  # big (A + B) , space Space O (A + B)


print("\n======== Merge two words ======")
print(f"merge words {word1} and {word2} is {mergeWord(word1, word2)}")

# =========== Matrix Transpose===========
print("\n============Transpose================")
"""Given an nxn 2D matrix representing an image, rotate the image by 90 degree clockwise"""
# Steps
# 1. Transpose operateion
# 2. swap firest and last col.

""" M =  [ 2 4 ] transpose == [ 2  5 ]  swap (1st & lst)cols  --> [ 5  2 ]
         [ 5 6 ]           == [ 4  6 ]                       -->  [ 6  4 ]
         
    """


def rotateMAtrix(matrix):
    n = len(matrix)

    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # step2 revesrs each row
    for i in range(n):
        matrix[i].reverse()

    # Swapping
    # for i in range(n):
    #     for j in range(n//2):
    return matrix


print(f'\n == == == == == == Rotate Image - Leetcode 48 - Arrays & Strings(Python)========\n')
matrix = [[2, 3, 4], [-1, 2, 4], [0, 9, 1]]
print(f'Matrix= {matrix}, is = {rotateMAtrix(matrix)}')


# Sort Colors --leetcode 75-----
print(f"===== Sort Colors ==== leetcode 75====")

""" Given an array nums with n objects colored red, white and blue, sorth thme in place..."""
# e.g [2,0,2,1,1,0] ==> [0, 0, 1, 1, 2, 2]
# soln--- DNF T==O(n) and S-- O(1)


def sortColor(nums):
    # using the counting sort....!
    counts = [0, 0, 0]

    for i in nums:
        counts[i] += 1
    r, b, w = counts
    nums[:r] = [0] * r
    nums[r:r+b] = [1] * b
    nums[r+b:] = [2] * w

    return nums


print(f"sort colors: {sortColor([2,0,2,1,1,0])}")


# # ========= letcode Sorted Squareds===========977
# Input1 = [-4, -1, 0, 3, 10]  # return sorted non-decreasing order
# # Output: [0, 1, 9, 16, 100]


# def sortedSqaure(nums):
#     # nums = [x**2 for x in nums]
#     # return sorted(nums)  # O(nlog n)

#     #using two pointers
#     l = 0
#     r = len(nums) -1
#     res = []

#     while l<=r:
#         if abs(nums[l]) > abs(nums[r]):
#             res.append(nums[l] ** 2)
#             l += 1
#         else:
#             res.append(nums[r] ** 2)
#             r -= 1
#     res.reverse()
#     return res


# print(f"Sorted Sqauredof {Input1} = {sortedSqaure(Input1)}")


print("\n==== Product and Sum of Array Except Selt=======")
""" 
--- [1,2,3,4] sum= 10
----[x,2,3,4] -- [9,] i,e 10 -1 =9, [9,8,..] i.e 10-2, [9,8,7] i.e 10-3,
--- [9,8,7,6] i.e 10-4=6
"""


def sumArray(nums):
    result = []
    totalSum = sum(nums)

    for i in nums:
        result.append(totalSum-i)
    return result


arr5 = [1, 2, 3, 4, 5]
print(
    f"Sum of Array {arr5} Except, where sum = {sum(arr5)}: {sumArray(arr5)} ")

print(f"\n ====== Product of Array Except========\n")


def productArray1(nums):
    result = []
    product = math.prod(nums)

    for i in nums:
        result.append(product//i)

    return result


print(f"Product of Array {arr5} except === {productArray1(arr5)}\n")


def productArray2(nums):
    n = len(nums)
    result = [1] * n
    # using prefix and postfix====
    prefix = 1
    suffix = 1

    for i in range(n):
        result[i] = result[i] * prefix
        prefix = prefix * nums[i]

    for i in reversed(range(n)):
        result[i] *= suffix
        suffix *= nums[i]

    return result


arr55 = [1, 2, 3, 4]
print(f"product of {arr55} except ifself = : {productArray2(arr55)} ")



#====== leetcode 88==== merge sorted Arrays ====

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]

