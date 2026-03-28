"""  2. 3Sum (VERY important) (sort + fix one element
two pointers inside) """

# Gvien array [-1,0,1,2,-1,-4] return num[i] + num[j] + num[k] ==0
# note: i != j, i != k, j!= k


def threeSum_brute(nums):
    n = len(nums)
    res = set()

    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                    res.add(triplet)
    return res


# tine = O(n^3)
arr = [-1, 0, 1, 2, -1, -4]
# ans = [[-1, -1, 2], [-1, 0, 1]]

print("========= Three Sum ===========")
print(f'Three Sum of {arr} === {threeSum_brute(arr)}')


""" ============== METHOD TWO and optimal---- Two pointers------

Steps====
1. sort the array
2. fix on element nums[i]
3. use two pointers (left and right) to find the other two

"""


def threeSum_pointer(nums):
    # step 1 sorting
    nums.sort()  # O(nlogn)
    n = len(nums)
    result = []

    #  step 2: loop through the array and fix one number
    for i in range(n):  # O(n)
        # skipping duplicates
        if nums[i] > 0 and nums[i] == nums[i-1]:
            continue

        # step 3: using the two pointers for other numbers

        l = i + 1  # left pointer
        r = n - 1  # right pointer

        while l < r:  # O(n)
            sum3 = nums[i] + nums[l] + nums[r]

            if sum3 == 0:
                result.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
                # inside the if-- skip duplicates to avoid adding same triplets
                while l < r and nums[l] == nums[l-1]:
                    l += 1
                while l < r and nums[r] == nums[r+1]:
                    r -= 1
            else:
                if sum3 < 0:
                    l += 1
                else:
                    r -= 1

    return result


# time = O(n log n) + O(n^2) = O(n^2), Space = O(n)

print(f'three Sum with pointer method: {threeSum_pointer(arr)}')
