# =========== Prodcut of Array Except itself ===============
"""   Question:
        1. Given an integer array nums, return an array answer such that answer[i] is equal to 
        the product of all elements of nums except nums[i]
         
         ===The product of any prefix or suffix of anums is `guaranteed` to fit in a 32-bit integer
         === time must O(n) and not division operataion
        
    
    """
nums = [1, 2, 3, 4]
# output = [24,12,8,6]

print("===================== Using division lol ============")


def prodArray(nums):
    res = []
    prod = 1
    for i in nums:
        prod *= i
    for i in nums:
        res.append(int(prod/i))
    return res


print(prodArray(nums))

print("\n ====== Using Brute Force Approach ==========")


def prodArray2(nums):
    res = []
    # prod = 1

    for i in range(len(nums)):
        prod = 1
        for j in range(len(nums)):
            if i != j:
                prod *= nums[j]
        res.append(prod)
    return res


print(prodArray2(nums))
