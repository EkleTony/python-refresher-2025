""" Merge Strings Alternately - Leetcode 1768 - Arrays & Strings (Python)

word1 = ab
words = pqrs

aqbqrs
 """


def mergeString(word1, word2):
    A, B = len(word1), len(word2)
    a, b = 0, 0
    st = []
    state = 1

    while a < A and b < B:
        if state == 1:
            st.append(word1[a])
            a += 1
            state = 2
        else:
            st.append(word2[b])
            b += 1
            state = 1
    while a < A:
        st.append(word1[a])
        a += 1
    while b < B:
        st.append(word2[b])
        b += 1
    return ''.join(st)


s1 = "abc"
s2 = "pqrstuv"

print(f'Merge Strings {s1} and {s2}: == {mergeString(s1, s2)}')
