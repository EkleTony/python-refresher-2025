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
