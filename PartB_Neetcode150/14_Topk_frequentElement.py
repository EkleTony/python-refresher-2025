# ============= TopK frequent Elements ==============
# Givne an interger array nums and an integer k, return the k most frquent elements.
# You may return the answer in any order
import heapq
from collections import Counter
print("==================== Solution 1: Using Counter =============")

nums = [1, 1, 1, 2, 2, 3]
k = 2
# output = [1,2]


def topKfreq(nums, k):
    count = Counter(nums)
    most_common = count.most_common(k)  # O(nlogn)
    res = [k for k, v in most_common]

    # for i, v in count.items():
    #     if v >= k:
    #         res.append(i)
    print(most_common)
    return res


print("Most Freq elelment at k = ", k, " are ", topKfreq(nums, k))


print("\n =============== Solution 2: Using Hashmap + Heap (Priority Queue) ====================")
# Hashmap: distinct value and occurrences
#
# Time : O(n), sorted a