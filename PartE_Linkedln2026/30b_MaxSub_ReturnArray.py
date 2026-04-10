"""  Maximum Subarray - Amazon Coding Interview Question - Leetcode 53 - Python

"""


def maxSum1(num):
    # Using Kadanes Algorithm...
    """ The Kadane's algorithm is a linear time-- algorithm used to fing hte maximum sum of a contigous subarray
    ----Key Idea: is that at each index, we only need to track the maximum subarray ending at the index.

    Step1 : 
    1. Define the State: "I ain a variable current_sum, which represents the maximum subarray sum ending at the current index.”
    2. At each element, I decide whether to:
       ---start a new subarray from the current element, or
       ---extend the previous subarray.”
    3. Recursion:  I take the max between the cur element itselt and the cur element plus the prev sum..
    4. I also track the global maximum that stores the best subarray seen so far.
    """
    cur_sum = num[0]
    max_sum = num[0]

    for i in range(1, len(num)):
        cur_sum = max(num[i], cur_sum + num[i])
        max_sum = max(cur_sum, max_sum)
    return max_sum


print(
    f'Maximum SubArry of {[-1, 2, 3, 6, -5]} is {maxSum1([-1, 2, 3, 6, -5])}')

print("=========== Return the SubArray too....!")
""" “So this gives me the maximum subarray sum in O(n) time and O(1) space.
If needed, I can extend this to also return the actual subarray by tracking indices.


===Idea: “To do that, I’ll keep track of where the current subarray starts,
           and whenever I find a new maximum, I’ll record its start and end positions.
           
           1. temp_start, best_start and best_end”"""
           
def maxSumArray2(num):
    # Return the max and the subarrays itself
    cur_sum = num [0]
    max_sum = num[0]
    
    # three variables
    temp_start = 0
    best_start = 0
    best_end = 0
    
    for i in range(1, len(num)):
        cur_sum = max(num[i], cur_sum + num[i])
        max_sum =  max(cur_sum, max_sum)
    return max_sum
