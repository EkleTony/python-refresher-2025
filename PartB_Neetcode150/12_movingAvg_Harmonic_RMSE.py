# Compute the moving average of a list using a sliding window of size k

import math


def movingAverage(nums, k):
    res = []
    for i in range(len(nums) - k+1):
        window = nums[i:i+k]
        avg = sum(window)/k
        res.append(avg)
    return res


print("========== Moving Average =============")
nums = [1, 2, 3, 4, 5, 6]
k = 3

print(f"nums: {nums} and k = {k}")
print(movingAverage(nums, k))


# ============= Hermonic Mean =============
# Hm = {n}/ sum{ 1/x_i}

def harmomicMean(nums):
    n = len(nums)
    deno = []
    for i in nums:
        deno.append(1/i)
    return n/sum(deno)


print("============Harmonic mean ============")
arr = [2, 3, 6]
x = harmomicMean(arr)
print(f"Harmonic Mean of {arr}  = {round(x, 3)}")


print(" \n=============The formula for RMSE (Root Mean Square Error) ===========")


def rsme(y_true, y_pred):
    n = len(y_true)
    diff = []
    for i in range(n):
        d = (y_true[i] - y_pred[i])**2
        diff.append(d)
    mse = sum(diff) / n
    # rmse = math.sqrt((1/n) * diff)
    return math.sqrt(mse)


# Example
y_true = [3, 5, 2.5, 7]
y_pred = [2.5, 5, 4, 8]

# print(f"RMSE = {round(rmse(y_true, y_pred), 3)}")
print("RMSE of", y_true, "and", y_pred, " = ", rsme(y_true, y_pred))
