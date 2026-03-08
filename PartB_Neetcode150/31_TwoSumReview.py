""" 
#============= Two Sum

--Given an array of integers nums and an integer target, return indices of `two numbers` 
---such that they add up to `target`

"""
# ---Attermpt


def twoSum1(arr1, target):
    for i in range(len(arr1)):
        for j in range(i, len(arr1)):
            if arr1[i] + arr1[j] == target:
                return [i, j]

# method 2 using pointers


def twoSum2(arr1, target):
    l = 0
    r = len(arr1) - 1
    while l < r:
        summ = arr1[l] + arr1[l]
        if summ == target:
            return [l, r]
        else:
            if summ < target:
                l += 1
            else:
                r -= 1


arr1 = [2, 3, 4, 5, 7, 5, 6, 8, 9]
target = 5
print("Two Sum and Target==", twoSum2(arr1, target))
