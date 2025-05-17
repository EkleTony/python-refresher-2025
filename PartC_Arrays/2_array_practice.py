# ================== 1. Sorting an Array ===============

nums = [3, 4, 5, 7, 1, 3, 5, 6]
nums.sort()  # O(nlogn)

print(nums)
print(nums.pop())


def findItem(arr):
    for i in arr:
        if i == 2 or i == 4:
            return True
        else:
            continue


x = findItem([1, 2, 5, 6, 7, 8])
print(x)
