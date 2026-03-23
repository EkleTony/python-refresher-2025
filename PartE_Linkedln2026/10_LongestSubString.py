""" Longest Substring Without Repeating Characters - Leetcode 3 - Sliding Window (Python)

Q: given a string s, find the lenght of the longest substrings without repeating chars...


"""

st = "abcabcbb"
# output = 3


def longestString(st):
    l = 0
    longest = 0
    seen = set()
    n = len(st)

    # a linear soln O(n)
    for r in range(n):
        while st[r] in seen:  # remember we only add i.e O(n)
            seen.remove(st[l])
            l += 1

        window = (r-l) + 1
        longest = max(longest, window)

        # add to the set
        seen.add(st[r])

    return longest
# time O(n)

print(f'Longest Substring: {longestString(st)}')