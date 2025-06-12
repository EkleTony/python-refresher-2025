# ============ Merge Strings  leetcode1768
""" 
    --Given two Strings w1 and w2, merge the strings by adding letters in alternating order,
    Starting with w1. if a string is longer than the other, append the additional letter onto the 
    end of the merged strings.
"""

st1 = "abcdef"
st2 = "pqr"

def mergeString(s1, s2):
    A, B = len(s1), len(s2)
    a, b = 0, 0
    s = []
    
    state = 1
    while a < A and b < B:
        if state ==1:
            s.append(s1[a])
            a += 1
            state =2
        else:
            s.append(s2[b])
            b += 1
            state = 1
    while a<A:
        s.append(s1[a])
        a += 1
    return ''.join(s)

print(mergeString(st1, st2))


print("\n ==================== TopK element =================")
# ============= TopK frequent Elements ==============
# Givne an interger array nums and an integer k, return the k most frquent elements.
# You may return the answer in any order

nums = [1,1,2,2,3,4,1,1,2,2,3,7,8,45,6,4,5,6]
from collections import Counter
def topKFreq(nums, k):
    counts = Counter(nums)
    
    common = counts.most_common()
    #topk = [key for key, v in common if v > k]
    topk = [key for key, v in counts.most_common(k)]
    
    return topk

print(topKFreq(nums, 2))

print("\n ========== UISing hash map and priority quuee for topkfreq===============")
from collections import Counter
import heapq

def topKFreq2(nums, k):
    count = {}
    minHeap = []
    for  i in range(len(nums)):
        count[nums[i]] = 1 + count.get(nums[i], 0)
    print(count)
    # next go throught
    #=== 2 Using MinHeap====
    for key, val in count.items():
        if len(minHeap) < k:
            heapq.heappush(minHeap, (val, key))
        else:
            heapq.heappushpop(minHeap, (val, key))
    return [h[1] for h in minHeap]
        
print(topKFreq2(nums, 2))

print("\n ======== is Palindrome =============")
s = "aBad"

def isPalin(st):
    # lower, check alpha-numeric, and reverse
    lst = []
    st = st.lower()
    for char in st:
        if char.isalnum():
            lst.append(char)
    
    return lst[::1] == lst[::-1]
            
print(isPalin(s))

print("\n ============== Two Sum ===============")
nums = [2, 7, 11, 15]
target = 13
# output = [0,1] i,e 2+7 = 9

def twoSum(nums, t):
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if (nums[i]+ nums[j]) == t:
                return [nums[i], nums[j]], " = ", [i, j]

print(twoSum(nums, target))

# method two using sliding windows
def twoSum2(nums, target):
    n = len(nums)
    left = 0
    right = n -1
    
    while left < right:
        summ = nums[left] + nums[right]
        
        if summ == target:
            return [nums[left], nums[right]], " = ", [left, right]
        else:
            if summ < target:
                left += 1
            else:
                right -= 1
print(f"Method 2: {twoSum2(nums, target)}")