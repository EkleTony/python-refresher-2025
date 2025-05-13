""" ================= Two Pointer Algorithm =============
1. The two pointer technique is a common algorithmic pattern where two variables (pointers) 
are used to iterate through a data structure (like a string or array), either:
2. From both ends inward (e.g., left and right)
3. In the same direction (e.g., slow and fast)
4. One fixed, one moving (like scanning or expanding)
"""
import math
# Exaple 1 ============  Square of a sorted array ================


def sortedSquares(arr):
    # input = [-4, -1, 0, 3, 10] and output = [0, 1, 9, 16, 100]
    sqrlst = sorted(i*i for i in arr)
    print(sqrlst)

    # Time: O(n log n)


# usingt Two pointesr

def sortedSquarePointer(arr):
    n = len(arr)
    l = 0
    r = n - 1
    result = []

    while l <= r:
        if abs(arr[l]) > abs(arr[r]):
            result.append(arr[l]**2)
            l += 1  # increase left pointer
        else:
            result.append(arr[r]**2)
            r -= 1
    # result.reverse() # reversing the list
    return result[::-1]

    # Time: O(n) and Space:


sortedSquares([22, 2, 4, -5])
print(sortedSquarePointer([-4, -1, 0, 3, 100]))  # [0,1,9,16,100]
