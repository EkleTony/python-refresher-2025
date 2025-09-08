"""You are given a list 'Data', which contains 99 numbers from 1:100 without repetition.
One of the number is missing from 1:100. Identify the missing number.
  """


data = [2, 3, 1, 5]  # output = 4


def missingArray(data):
    n = len(data) + 1  # O(n)
    sumNum = (n * (n + 1)) / 2  # (n(n+1))/2
    return sumNum - sum(data)


print(f'=====Finding One Missing Number========! ')
print(missingArray(data))

# [2,3,5] # 4,1


def twoMissingNum(data):

    n = len(data) + 2
    missingSum = ((n*(n+1))//2) - sum(data)

    # idea: is to find the missing two
    # we know that (A+B)/2 = avg of missing values i.e 5//2 = 2
    # hence assume the value are slitted into 1st half and 2nd half
    # i.e [2,3,5] nums <= 2 or nums > 2
    avg = missingSum//2
    avgSummFirstHalf = (avg * (avg + 1) // 2)
    sumFirstHalf = sum(i for i in data if i <= avg)

    value1 = avgSummFirstHalf - sumFirstHalf
    value2 = missingSum - value1
    print(missingSum)

    return value1, value2


data2 = [1, 2, 3, 5, 7, 8]  # 4,6 = 10
print("Two Missing Sum: ", twoMissingNum(data2))

# A + B = 5
# AB = ?

print("\n============= Find the single number =-- Bit MAnipulation =================")
num = [1, 2, 3, 1, 2, 3, 4, 5, 5]

print(2 ^ 2)


def singleNum(num):
    a = 0
    for n in num:
        a ^= n
    return a


print("Single num is: ", singleNum(num))
