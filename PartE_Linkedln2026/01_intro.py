# ========== Preparing for Coding interivew please ================
"""
=========== DS ====Core patterns:=====
1. HashMap / Dictionary
2. Sliding window
3. Two pointers
4. Heap (top K problems)
5. BFS / DFS
6. Simple dynamic programming

"""


#========Question 1===
"""Q1:  Given an integer array num and an interger k return the k most freq elements.
e.g,
nums = [1,1,1,2,2,3] k=2, output = [1,2]

"""
from collections import Counter
def topK(num, k):
    n = len(num)
    ans = []
    count = Counter(num)
    ans.append([i for i, k in count.items() if k>1])
    return ans
    

nums = [1, 1, 1, 2, 2, 3] 
k = 2
print(topK(nums, k))
    


