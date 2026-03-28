"""  2. 3Sum (VERY important) (sort + fix one element
two pointers inside) """

# Gvien array [-1,0,1,2,-1,-4] return num[i] + num[j] + num[k] ==0
# note: i != j, i != k, j!= k


def threeSum_brute(nums):
    n = len(nums)
    res = []

    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    res.append([nums[i], nums[j], nums[k]])
    return res


# tine = O(n^3)
arr = [-1, 0, 1, 2, -1, -4]
# ans = [[-1, -1, 2], [-1, 0, 1]]

print("========= Three Sum ===========")
print(f'Three Sum of {arr} === {threeSum_brute(arr)}')
