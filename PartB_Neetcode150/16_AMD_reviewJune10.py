# ========== REviewoing my codes ============

# 1. Find Closest Number to Zero - Leetcode 2239 - Arrays & Strings (Python)
from collections import defaultdict
from collections import Counter
nums = [-4, -2, 1, -1, 4, 8]
# nums = [5, -5]
# nums = [0, -1, 1]

print("============== Closest to Zero ================")


def findClosestNumber(nums):
    closest = nums[0]
    result = []
    for num in nums:
        if (abs(num) < abs(closest) or abs(num) == abs(closest)) and num > closest:
            closest = num
    return closest


print(findClosestNumber(nums))


# 2 Is Anagram ======
print("\n ================= Is Anagram ==================== ")


def isAnagram(st1, st2):
    return Counter(st1) == Counter(st2)


st1 = "eat"
st2 = "ate"
print(isAnagram(st1, st2))

print("\n ==== Using HashMap====")


def isAnagram2(st1, st2):
    # case with different lenght
    if len(st1) != len(st2):
        return False
    # buiding a hashmap
    count1 = {}
    count2 = {}

    for i in range(len(st1)):
        count1[st1[i]] = 1 + count1.get(st1[i], 0)
        count2[st2[i]] = 1 + count2.get(st2[i], 0)
    print(count1)
    print(count2)
    # now check if both are anagram
    if count1 == count2:
        return True


print(isAnagram2(st1, "atea"))


def isAnagram3(st1, st2):
    if sorted(st1) == sorted(st2):
        return True


print(isAnagram3(st1, st2))


print("\n===========================GROUP ANAGRAM !======================================")
st = ["eat", "tea", "tan", "ate", "nat", "bat"]
# Output: [["eat","tea","ate"],["tan","nat"],["bat"]]
print(" Original Strings: ", st)


def groupAnagram(st):
    anagram = defaultdict(list)

    for word in st:
        key = ''.join(sorted(word))
        anagram[key].append(word)
    return list(anagram.values())


print("Grouped Anagram: ", groupAnagram(st))
