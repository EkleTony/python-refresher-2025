# ======= Given two strings return True if s and t are anagram ===
from collections import Counter
from collections import defaultdict


def groupAnagram(st):
    anagram = defaultdict(list)

    for cha in st:
        keys = ''.join(sorted(cha))
        anagram[keys].append(cha)
    res = [True for k, v in anagram.items() if len(v) > 1]
    return res


st = ["eat", "tea", "tan", "ate", "nat", "bat"]
# Output: [["eat","tea","ate"],["tan","nat"],["bat"]]


def isAnagram(s, t):
    return Counter(s) == Counter(t)


print(isAnagram("eat", "tea"))
