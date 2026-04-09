""" Merge Strings Alternately - Leetcode 1768 - Arrays & Strings (Python)

word1 = ab
words = pqrs

aqbqrs

STEPS
1. Initialize two pointers a and b for both strings.
2. Create an empty list st to store the result.
3. Loop while both pointers are within bounds.
4. Alternate picking characters from each string.
5. Move the corresponding pointer after each pick.
6. Append remaining characters from word1 if any.
7. Append remaining characters from word2 if any.
8. Join the list into a final string and return.
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
