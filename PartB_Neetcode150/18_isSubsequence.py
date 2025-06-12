# =========== Is Subsequence leetcode 392 ==============
s = "acfg"
t = "abcdf"

def isSubsequence(s, t):
    S = len(s)
    T = len(t)
    
    if s=="": return True
    if S > T: return False
    
    count = 0
    for i in range(len(t)):
        if t[i] == s[count]:
            if count == len(s) -1: # last index of s
                return True
            count += 1
    return False

print(isSubsequence(s, t))

print("\n================ ThreeSum equal to zero ===========")