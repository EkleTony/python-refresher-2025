"""" 🔥 8. Top K Frequent Elements"""


import heapq
from collections import Counter
num = [1, 1, 2, 2, 3, 4, 4, 4, 4, 4]

k = 3  # ans = [4,1,2]

# using counter or hashmap and get the most k freq
# O(nlog n)


def topKFreqElement1(num, k):
    count = Counter(num)  # {1:2, 2:2, 3:1, 4:5}
    most_common = count.most_common(k)
    topk = [num for num, freq in most_common]
    return topk


"""“I’m using Counter to build the frequency map, 
then extracting the top k elements based on frequency. 
Internally, this uses sorting, so the time complexity is O(n log n).”"""


num3 = [1, 1, 1, 2, 2, 3, 4, 4, 4]

print(f"Top K {2} of {num3} is ==  {topKFreqElement1(num3, 2)}")


"""=========METHOD 2: USING HEAP........!"""


def topK(nums, k):
    # count = Counter(nums)  # {1:3, 2:2, 3: 1, 4:3}
    # most_common = count.most_common(k)
    # topk = [num for num, freq in most_common]
    # return topk
    ''' Using Heap....'''
    freq = Counter(nums)
    heap = []

    for num, count in freq.items():
        heapq.heappush(heap, [count, num])
        # [ (1,3), (2,2),  (3,1), (3,4)]

        if len(heap) > k:
            heapq.heappop(heap)

    return [num for count, num in heap]


print(f"Most freqent in {num3} is ----NEW==== {topK(num3, 2)}")


def topKfreqelement2(nums, k):
    freq = Counter(nums)  # {1:3, 2:2, 3:1, 4:3}
    heap = []

    for num, count in freq.items():
        # Heap will organize based onthe min..frequency..
        heapq.heappush(heap, [count, num])
        # heap = [[3,1], [2,2], [1:3], [3,4]]

        # ...Then we pop.. the first elements..
        if len(heap) > k:
            heapq.heappop(heap)
        # ==poping front--> [(3,1)] --> [(2,2), (3,1)]
        # --> [(1,3), (3,1), (2,2)] --> is k>2 pop [(2,2), (3,1)]
        # --next (3,4)--> pop smallest (2,2) -->[(3,1), (3,4)]
    return [num for count, num in heap]


print("=========== topk using Heap......!")
print(f"TopK Freq. Element: in {num3} == {topKfreqelement2(num3, 2)}")


"""============ Method 3===== Using Bucket Sort---O(n) answer...!"""


def TopK_bucketSort(nums, k):
    n = len(nums)
    counter = Counter(nums)
    bucket = [0] * (n+1)

    for num, freq in counter.items():
        if bucket[freq] == 0:
            bucket[freq] = num
        else:
            bucket[freq].append(num)

    # back-track and return topk
    lst = []
    for i in range(n, -1, -1):
        if bucket[i] != 0:
            lst.extend(bucket[i])
        if len(lst) == k:
            break
    return lst


num4 = [1, 1, 1, 2, 2, 3, 4, 5, 3, 3, 4, 5, 6, 2, 1, 3]
print("\n===================================================")
print(f"====TopK Elements===== {num3} is {TopK_bucketSort(num3, 2)}")

# def maxMin(nums):
#     minn = nums[0]
#     maxx = nums[0]
#     for num in nums:
#         if num <= minn:
#             minn = num
#         if num >= maxx:
#             maxx = num

#     return minn, maxx


# print("\n")
# print(f"Min and Max in {num2} is === {maxMin(num2)}")

# def returnDupicate(nums):
#     check = set()
#     duplicate = set()
#     for num in nums:
#         if num in check:
#             duplicate.add(num)
#         check.add(num)
#     return list(duplicate)
# print(f"Return duplicate in {num2} === {returnDupicate(num2)}")
print("\n=====")
print("\n============ Other Questions=============")
# num2 = [1, 2, 6, 7, 8, 9, 1, 1, 1, 2, -5]

"""==== Best Time to Buy and Sell Stock------
Q1: Given an array prices where preces[i] is the stock price aon day i, return the maximum profit you can 
  achieve by choosing one day to buy and a later day to sell.
  

"""
prices = [7, 1, 5, 3, 6, 4]


def buyStock1(prices):
    max_profit = 0

    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            profit = prices[j] - prices[i]
            max_profit = max(max_profit, profit)
    return max_profit


def buyStock2(prices):
    min_price = num[0]
    max_profit = 0

    for price in prices[1:]:
        if price < min_price:
            min_price = price

        else:
            profit = price - min_price
            max_profit = max(max_profit, profit)
    return max_profit


def buyStock_kadane(prices):
    max_profit = 0
    cur_sum = 0
    for i in range(1, len(prices)):
        diff = prices[i] - prices[i-1]
        cur_sum = max(0, cur_sum + diff)
        max_profit = max(max_profit, cur_sum)
    return max_profit


print(f"Profits--BruteForce: {prices} = {buyStock1(prices)}")
print(f"Profits--Optimal: {prices} = {buyStock2(prices)}")
print(f"Profits--Kadane's: {prices} = {buyStock_kadane(prices)}")
