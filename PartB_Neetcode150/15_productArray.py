# ============= Product of Array Except self ===================
"""   Question:
        1. Given an integer array nums, return an array answer such that answer[i] is equal to the product
         of all elements of nums except nums[i]
         
         ===The product of any prefix or suffix of anums is `guaranteed` to fit in a 32-bit integer
         === time must O(n) and not division operataion
        
    
    """
nums = [1, 2, 3, 4]
# output = [24,12,8,6]

# Steps
# 1. Get the product before i (prefix) and product after i (postfix)
# 2. prefix ()
prod = 1
res = []
for i in nums:
    prod *= i
for i in nums:
    res.append(int(prod/i))
print("product: ", prod)
print(res)

n = len(nums)

print("\n ===== Using Brute Force appraoch ========")


def productArray(nums):
    res = []
    n = len(nums)

    for i in range(n):
        prod = 1
        for j in range(n):
            if i != j:
                prod *= nums[j]
        res.append(prod)
    return res


x = productArray(nums)
print(x)
# Time: O(n^2)

print("\n ================= Using the Prefix and Postfix ==============")


def productArray2(nums):
    n = len(nums)
    res = [1] * n
    prefix = 1
    for i in range(n):
        res[i] = prefix
        prefix *= nums[i]
    print(res)
    # postfix
    postfix = 1
    for i in range(n-1, -1, -1):
        res[i] = postfix
        postfix *= nums[i]

    return res


print(productArray2(nums))

print("\n =========Two Sum Review =====")
nums = [1,2,3,6]
target = 9


def twoSum(nums, target):
    n = len(nums)
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement not in seen:
            return [seen[complement], 1]
    seen[num] = i
    return seen
            
        
    # bRute force apporache
#     for i in range(n):
#         for j in range(i, n):
#             if (nums[i] + nums[j]) == target:
#                 return [[i, j], [nums[i], nums[j]]]

print(twoSum(nums, target))

# using prefix and postfix
