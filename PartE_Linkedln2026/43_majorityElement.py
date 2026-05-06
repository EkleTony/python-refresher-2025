""" Majority Element - Leetcode 169 - Hashmaps & Sets (Python)
 """

from collections import Counter


def mostFreqElement(arr):
    counts = Counter(arr)  # {2:2, 3:3, 4: 2, 1:1}
    # most_common = [val for val, count in counts.most_common(1)]
    return counts.most_common(1)[0][0]


def majorityElement(arr):
    counts = Counter(arr)
    n = len(arr)
    for val, count in counts.items():
        if count > n//2:
            return val
    return None

def majorityOptimalCode(nums):
    ans = None
    count = 0
    
    
    for num in nums:
        if count ==0 :
            ans = num
        if ans == num:
            count += 1
        else:
            count -= 1
    return ans

num = [2, 3, 3, 4, 4, 4, 4]
print(f"Most Frequent Element  in {num} is == {mostFreqElement(num)}")
print(f"Majority Elements in {num} is === {majorityElement(num)}")
print(f"Majority Elements Optimal in {num} is === {majorityOptimalCode(num)}")
