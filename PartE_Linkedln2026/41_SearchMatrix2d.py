""" ========== Search a 2D Matrix - Leetcode 74 - Python  ==========

***Given mxn matrix. The matrix has the folliwign properties...

--integeger in each row are sorted from left to right
---the first integer of each row is greate than the last integer of the prev row.

"""

"""===Using Double Binary Search...!"""

nums = [-1, 0, 35, 9, 12]
t = 35


def binarySearch(arr, t):
    n = len(arr)
    l = 0
    r = n-1
    while l < r:
        mid = (l+r)//2
        if arr[mid] == t:
            return mid
        elif arr[mid] > t:
            r = mid - 1

        else:
            l = mid + 1
    return -1


print(f'========Binary Search=====')
print(
    f'\n === Given {nums} and target {t}, Binary Search is {binarySearch(nums, t)}')


def searchMatrix2D(matrix, target):
    rows = len(matrix)
    cols = len(matrix[0])
    top, bot = 0, rows-1  # two pointers
    while top <= bot:
        row = (top + bot) // 2
        if target > matrix[row][-1]:
            bot = row + 1

        elif target < matrix[row][0]:
            top = row - 1
        else:
            break
    if not (top <= bot):
        return False
    row - (top + bot) // 2
    l, r = 0, cols - 1
    while l < r:
        m = (l + r)//2
        if target > matrix[row][m]:
            l = m + 1
        elif target < matrix[row][m]:
            r = m - 1
        else:
            return True
    return False


matrix = [[1, 3, 5, 7],
          [10, 11, 16, 20],
          [23, 30, 34, 60]]
target = 3

print(f"========= Matrix Search=====")
print(f" given {matrix} and target {target}.... location is {searchMatrix2D(matrix, target)}")