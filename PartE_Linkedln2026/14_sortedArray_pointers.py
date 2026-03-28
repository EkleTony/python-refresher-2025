""" ============ Sorted Array---

given [1,-2,-5,6] return square of sorted array
"""


def sortedArray(nums):
    # iterate of and cal square of each
    # return sorted list

    res = []
    for x in nums:
        res.append(x**2)
    return sorted(res)


print("============== Sorted Array--------- method 1 O(nlog n)")
arr = [-1, 2, 3, -5, 8, 4]
print(f'Sorted Array with loop and sorting: {sortedArray(arr)}')
print()

print("========Method two with pointers =========")


def sortedArray2(nums):
    left = 0
    right = len(nums) - 1
    res = []

    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            res.append(nums[left] ** 2)
            left += 1
        else:
            res.append(nums[right]**2)
            right -= 1
    res.reverse()
    return res


print(f'Sorted Array using Two pointers: {sortedArray2(arr)}')
