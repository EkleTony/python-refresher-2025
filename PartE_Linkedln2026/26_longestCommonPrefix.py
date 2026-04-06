""" 
Longest Common Prefix - LeetCode 14 

 
"""

# output = "fl"


def longestCommonPrefix(strs):
    prefix = strs[0]
    for i in range(len(prefix)):
        for word in strs:
            if i == len(word) or prefix[i] != word[i]:
                return prefix[:i]
    return prefix


strs = ["flower", "flow", "flight"]









def longCommon(st):
    # pick first word as references
    # compare ch by ch
    # stop at first mismatch 
    # return prefix so far
    prefix = st[0]
    for i in range(len(prefix)):
        for word in st:
            if i == len(word) or prefix[i] != word[i]:
                return prefix
            