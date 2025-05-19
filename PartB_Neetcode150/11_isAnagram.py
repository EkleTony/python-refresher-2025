# =============== given two string check if they're anagram ===========

from collections import Counter


def isAnagram(st1, st2):
    if Counter(st1) == Counter(st2):
        return True
    return False


st1 = "ate"
st2 = "nea"

print(isAnagram(st1, st2))

#

# ================== Using hash map ====
print('=============Using HashMap (Interview Standard!  )=============')


def isAnagram2(s1, s2):
    # 1. check fi both lengths are equal
    if len(s1) != len(s2):
        return False

    #2  building hashmap
    count1 = {}
    count2 = {}
    for i in range(len(s)):
        
        count1[s1[i]] = 1 + count1.get(s1[i], 0)
        count2[s2[i]] = 1 + count2.get(s2[i], 0)
        
    # 3. iterate through the hashmap to see if the counts are same
    #
    print(cout1, count2)
    

isAnagram2(st1, st2)
