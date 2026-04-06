""" Palindrome Number - Leetcode 9 - Python

NB: no converting to string... (with string use ponters easy )
"""

# step still using twop pointers


def palindromeNumber(num):
    """ idea
    1. x = 121 ans: true
    2.... using mod operation or int division
    """
    # bruteforce
    if str(num) == str(num)[::-1]:
        return True
    return False


def optimal(num):
    """ Idea: Reverse only half of the number and compare both sides....! """
    pass


print(f"1221%10 = {1221 % 10}")
print(f"1221//10 = {1221//10}")

nu1 = 121
num = -121

print(f'Is {num} palindrome number? == {palindromeNumber(num)} ')
