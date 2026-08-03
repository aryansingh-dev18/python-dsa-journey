"""
Problem: LeetCode 344 - Reverse String

Topic:
- Two Pointers

Difficulty:
- Easy

Approach:
- Place one pointer at the beginning and another at the end.
- Swap both characters.
- Move the left pointer forward and the right pointer backward.
- Continue until both pointers meet.

Time Complexity:
- O(n)

Space Complexity:
- O(1)

Author:
- Aryan Singh

Date:
- 03/08/2026
"""

s = ["h","e","l","l","o"]

left = 0
right = len(s)-1

while left < right:
    s[left],s[right] = s[right],s[left]

    left += 1
    right -= 1
print(s)