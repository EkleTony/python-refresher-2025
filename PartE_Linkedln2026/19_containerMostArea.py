"""  ======Leetcode 11 ====== Container With Most Water=======

You are given an integer array height of length n.

There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

"""

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
# Output: 49
# Explanation:
# The max area is formed between height[1] = 8 and height[8] = 7.
# Width = 8 - 1 = 7
# Height = min(8, 7) = 7
# Area = 7 * 7 = 49


def containerMostWater(height):
    left = 0
    right = len(height) - 1
    max_water = 0

    while left < right:
        # finding the max area
        width = right - left
        cur_height = min(height[left], height[right])
        area = width * cur_height

        # updating the max area
        max_water = max(max_water, area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_water


print(f'Contain with most water {height} is = {containerMostWater(height)}')
