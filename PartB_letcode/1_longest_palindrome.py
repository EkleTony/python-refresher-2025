# ============== Valid Palindrome ===============

def longestPalindrome(st):
    # input = babad and output = bab
    # n = len(st)
    # maxlen = 0
    # result = ""
    # for i in range(n):
    #     for j in range(i, n):
    #         substr = st[i:j+1]
    #         if substr[::1] == substr[::-1]:
    #             if len(substr) > maxlen:
    #                 maxlen = len(substr)
    #                 result = substr
    # return result

    # ===== Using Two pointers =======
    result = ""
    maxlen = 0
    n = len(st)
    for i in range(n):
        # odd lengths
        l, r = i, i  # at the center
        while l > 0 and r < n and st[l] == st[r]:
            if (r-l+1) > maxlen:
                maxlen = r-l+1
                result = st[l:r+1]
            l -= 1
            r += 1
        # even lengths
        l, r = i, i+1
        while l > 0 and r < n and st[l] == st[r]:
            if (r-l+1) > maxlen:
                result = st[l:r+1]
                maxlen = r-l+1
            l -= 1
            r += 1
    return result


print(longestPalindrome("babad"))
