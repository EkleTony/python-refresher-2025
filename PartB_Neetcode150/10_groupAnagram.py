# ======= Given two strings return True if s and t are anagram ===
from collections import Counter
from collections import defaultdict


def groupAnagram(st):
    anagram = defaultdict(list)
    res = []

    for cha in st:
        keys = ''.join(sorted(cha))  # O(nlogn)
        anagram[keys].append(cha)
    # res = [res.append(v) for k, v in anagram.items()]
    for k, v in anagram.items():
        res.append(v)  # O(n)
    # t = len(res) >1
    return res, len(res) > 1     # O(k)


st = ["eat", "tea", "tan", "ate", "nat", "bat"]
# Output: [["eat","tea","ate"],["tan","nat"],["bat"]]
print(groupAnagram(st))


def isAnagram(s, t):
    return Counter(s) == Counter(t)


print(isAnagram("eat", "tea"))


# ============== using Hashmap and set ============ O(n)


def groupAnagram2(st):
    # default dict
    anagram_dict = defaultdict(list)

    for word in st:
        count = [0]*26  # count list of 26 char

        # now loop each word
        for char in word:
            count[ord(char) - ord('a')] += 1
        key = tuple(count)
        print(key)
        anagram_dict[key].append(word)

    print(anagram_dict.values())


# Time: loop 1 ==n, inner loop, if max(st) = m
#  i.e n*m = O(n*m)
# Space= (n*m)
print("=============== Using Hashmap and set =================")
print(st)
groupAnagram2(st)
