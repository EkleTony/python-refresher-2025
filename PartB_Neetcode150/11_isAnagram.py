# =============== given two string check if they're anagram ===========

from collections import defaultdict
from collections import Counter

print("================ Using Counter =============")


def isAnagram(st1, st2):
    if Counter(st1) == Counter(st2):
        return True
    return False


st1 = "ate"
st2 = "tea"

print(isAnagram(st1, st2))

#

# ================== Using hash map ====
print('=============Using HashMap (Interview Standard!  )=============')


def isAnagram2(s1, s2):
    # 1. check fi both lengths are equal
    if len(s1) != len(s2):
        return False

    # 2  building hashmap
    count1 = {}
    count2 = {}
    for i in range(len(s1)):

        count1[s1[i]] = 1 + count1.get(s1[i], 0)
        count2[s2[i]] = 1 + count2.get(s2[i], 0)

    # 3. iterate through the hashmap to see if the counts are same
    for c in count1:
        if count1[c] != count2.get(c, 0):
            return False
    print(count1, count2)
    return True


print(isAnagram2(st1, st2))

print("\n ========= using Sorting =========== O(nlgn)")


def isAnagram3(st1, st2):
    if sorted(st1) == sorted(st2):
        return True
    return False


# time = O(nlogn)
# space = O(1)
print(isAnagram3("nta", st2))


print("\n ========== Using the HashMap again ===========")


def isAnagram4(s1, s2):
    """_summary_ === Using hashmap---

    Steps:
        1. first check if both strings are equal or not
        2. use hash map and count each occurrences
        3. compare the two hashmaps 
    """
    if len(s1) != len(s2):
        return False
    count1 = {}
    count2 = {}

    # building the hash map
    for i in range(len(s1)):
        count1[s1[i]] = 1 + count1.get(s1[i], 0)
        count2[s2[i]] = 1 + count2.get(s2[i], 0)
    # for k in count1:
    #     if count1[k] != count2.get(k, 0):
    #         return False
    print(count1, count2)
    return count1 == count2


    # print(count1, count2)
print(isAnagram4(st1, st2))


# =============== Group Anagram
print("\n")
print("============ GROUP ANAGRAM ==================")
st = ["eat", "tea", "tan", "ate", "nat", "bat"]
# Output: [["eat","tea","ate"],["tan","nat"],["bat"]]

# using 1) defualtdict and 2) using complement


def groupAnagram(st):
    anagram = defaultdict(list)

    for word in st:
        key = ''.join(sorted(word))  # O(nlogn)
        anagram[key].append(word)
    # for k, v in anagram.values():
    #     return anagram.values
    # print(anagram)
    return list(anagram.values())


print(groupAnagram(st))
print("\n")
print("============= Using HAsh set and complement ===========")
def groupAnagram2(st):
    anagram = defaultdict(list)
    
    # create count of 26 array
    for word in st:
        count = [0] * 26
        
        for char in word:
            count[ord(char) - ord('a')] += 1
        key = tuple(count)
        anagram[key].append(word)
        print(key)
    return anagram.values()
        
        
        
    
    
    
print(groupAnagram2(st))