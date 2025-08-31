# Product of Arracy except ==========

nums = [1,2,3,4] # output: [24,12,8,6]
def productArrayExcept(nums):
    suffix = 1
    result = [1] * len(nums)
    prefix = 1
    for i in range(len(nums)):
        result[i] *= prefix
        prefix *= nums[i]
        
    for i in reversed(range(len(nums))):
        result[i] *= suffix
        suffix *= nums[i]
    return result

def arraySumm(nums):
    result = []
    #1. sum all arraya
    #2. and substract each by iterating that will be sum for the others
    totalSum = sum(nums)
    for num in nums:
        result.append(totalSum - num)
    return result

print("Sum Except: ", arraySumm(nums))

print("\n ======= Product Array Except ===========")
print(f"Array = {nums}")
print(productArrayExcept(nums))

