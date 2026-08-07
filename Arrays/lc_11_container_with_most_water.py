"""
Problem: LeetCode 11 - Container With Most Water

Topic:
- Two Pointers

Difficulty:
- Medium

Approach:
- Use two pointers, one at the beginning and one at the end.
- Calculate the water contained between the two lines.
- Update the maximum area if needed.
- Move the pointer with the smaller height inward.
- Continue until both pointers meet.

Time Complexity:
- O(n)

Space Complexity:
- O(1)

Author:
- Aryan Singh

Date:
- 07/08/2026
"""


height = [1,8,6,2,5,4,8,3,7]

left = 0
right = len(height)-1
max_area  = 0


while left < right:
    area = (right - left )* min(height[left],height[right])
    max_area = max(max_area,area)

    if height[left] < height[right] :
        left += 1

    else:
        right -= 1

print(max_area)