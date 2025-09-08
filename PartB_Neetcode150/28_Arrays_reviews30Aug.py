# ======== closest to zero====
def findClosestNum(num):
    closest = num[0]
    for x in num:
        if abs(x) < abs(closest):
            closest = x
    if closest < 0 and abs(closest) in num:
        return abs(closest)
    return closest


num = [-4, -1, 1, 2, 3, 4, -2]
print("Closest num to zero in ", num, " is =: ", findClosestNum(num))

# == 02 ===Merge Strings Alternately - Leetcode 1768 - Arrays & Strings (Python)
num2 = [-3, -2, -1, 2, 3, 5]


def sortedSquare(num):
    # using two-pointers
    left = 0
    right = len(num) - 1
    result = []
    while left <= right:
        if abs(num[left]) > abs(num[right]):
            result.append(num[left]**2)
            left += 1
        else:
            result.append(num[right] ** 2)
            right -= 1
    result.reverse()
    return result


print(sortedSquare([-4, -1, 0, 3, 10]))


# ======== 3 Merge String============
def mergeString(str1, str2):
    left = 0
    right =
