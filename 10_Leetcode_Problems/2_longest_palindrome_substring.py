""" =========== Longest Palindrome Substring ==================
    1. Given a string s, find the longest palindrome substring in s, you may assume that the maximum length 
    of s is 1000.

    Example 1:
    input: babad
    output = bab
    note: aba is also a valid answer
    """

# ============== 1.  Brute Force ====================


def longest_palindrome1(st):
    result = ""
    maxlen = 0  # longest length

    for i in range(len(st)):
        for j in range(i, len(st)):
            substr = st[i:j+1]  # each substrings
            if substr == substr[::-1]:  # palindrome
                # check if substr is longest
                if len(substr) > maxlen:
                    maxlen = len(substr)
                    result = substr
    return "longest palindrome is: ", result
    # Complexity: O(n³): O(n²) substrings × O(n) to reverse and compare

# ================= Optimized Solution =====================


def longest_palindrome2(st):
    result = ""
    maxLen = 0
    n = len(st)

    for i in range(len(st)):
        # odd length
        l, r = i, i  # center postion for now

        while l >= 0 and r < n and st[l] == st[r]:
            if (r-l+1) > maxLen:
                result = st[l:r+1]  # update the longest pali result
                maxLen = r-l+1  # update the maxlenght
            l -= 1
            r += 1
        # even length
        l, r = i, i+1
        while l >= 0 and r < n and st[l] == st[r]:
            if (r-l+1) > maxLen:
                result = st[l:r+1]
                maxLen = r-l+1
            l -= 1
            r += 1
    return result

    # Examples
    # print(f"longest palindrome is {"hellow"}")
x = longest_palindrome1("badaad")
print(x)

y = longest_palindrome2("baddadadadadfa")
print(f"Two pointers: ", y)
