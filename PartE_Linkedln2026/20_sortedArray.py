""" ============== Merge Sorted Array - LeetCode 88=============

You are given two integer arrays:

---nums1 of size m + n, where:
---the first m elements are sorted and 
---the last n elements are 0 (empty space)
---nums2 of size n, sorted
🎯 Task
Merge nums2 into nums1 as one sorted array in-place."""

nums1 = [-1, 1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]


def sortedArray(nums1, m,  nums2, n):
    # step using 3 pointers, p1, p2, p3...
    # assigne p1 and p2 to end of nums1 and nums2 and p3 to end of dummy variable in nums2
    # while p1 and p1 are not empty, add the highest element in both num1 and num2 from the back of num1
    # and place the largest at the end
    p1 = m - 1
    p2 = n - 1
    p3 = m + n - 1

    while p1 >= 0 and p2 >= 0:

        if nums1[p1] > nums2[p2]:
            nums1[p3] = nums1[p1]
            p1 -= 1
        else:
            nums1[p3] = nums2[p2]
            p2 -= 1
        p3 -= 1
    while p2 >= 0:
        nums1[p3] = nums2[p2]
        p2 -= 1
        p3 -= 1


print(
    f'Sorted Array of {nums1} and {nums2} is == {sortedArray(nums1, 4, nums2, 3)}')
print(nums1)
