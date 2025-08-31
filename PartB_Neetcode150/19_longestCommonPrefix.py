# ========== Longest Common Prefix =======
print("\n ================= LOngest Comment prefix ==============")
st = ["flower", "flow", "flight"]
st2 = ["dog", "race", "eat"]  # output: ""
# output: "fl"

""" Steps:

1. Compare other strings with the first one
2. what if not equal size (Check min length first)
3. if minLen =4, no checking after that.

"""


def longestCommonPrefix(strs):
    minLen = len(strs[0])  # float('inf')

    # find the string with min length
    for s in strs:
        if len(s) < minLen:
            minLen = len(s)
    # comparing the prefixs

    c = 0
    while c < minLen:
        for s in strs: 
            if s[c] != strs[0][c]:
                return s[:c]
    # increase count
        c += 1
   # return s[:c]
# Time = O(n*m)


print(st)
print("Min Length: ", longestCommonPrefix(st))
