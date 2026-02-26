# ============ Merged String ===========
def mergeString(s1, s2):
    A, B = len(s1), len(s2)
    a, b = 0, 0
    s = []

    word = 1
    while a < A and b < B:
        if word == 1:
            s.append(s1[a])
            a += 1
            word = 2
        else:
            s.append(s2[b])
            b += 1
            word = 1
    while a < A:
        s.append(s1[a])
        a += 1
    while b < B:
        s.append(s2[b])
        b += 1

    return "".join(s)  # Time: O(A + B), space O(A+B)


word1 = "abc"
word2 = "pqrs"
print(mergeString(word1, word2))
