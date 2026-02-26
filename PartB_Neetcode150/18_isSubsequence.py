# =========== Is Subsequence leetcode 392 ==============
s = "acfg"
t = "abcdf"


def isSubsequence(s, t):
    S = len(s)
    T = len(t)

    if s == "":
        return True
    if S > T:
        return False

    count = 0
    for i in range(len(t)):
        if t[i] == s[count]:
            if count == len(s) - 1:  # last index of s
                return True
            count += 1
    return False


print(isSubsequence(s, t))

print("\n================ ThreeSum equal to zero ===========")
# examples
arr = [-3, -3, -2, -1, 0, 1, 2, 2, 3]
# output = [-1, 1, 0] = 0, []


def threeSum3(arr):
    # sorting
    # duplicate check
    # pointer and duplication check and increament
    arr.sort()                # === O(nlogn)
    res = []
    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i-1]:
            continue  # skip if duplicated occur

        left = i + 1
        right = len(arr) - 1

        while left < right:
            summ = arr[i] + arr[left] + arr[right]
            if summ == 0:
                res.append([arr[i], arr[left], arr[right]])

                # check duplicates
                while left < right and arr[left] == arr[left+1]:
                    left += 1
                while left < right and arr[right] == arr[right-1]:
                    right -= 1
                    # increasing pointers
                left += 1
                right -= 1
            elif summ < 0:
                left += 1
            else:
                right -= 1

    return res


print(threeSum3(arr))
