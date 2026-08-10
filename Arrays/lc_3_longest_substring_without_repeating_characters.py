"""
Problem: LeetCode 3 - Longest Substring Without Repeating Characters

Topic:
- Sliding Window
- Set

Difficulty:
- Medium

Approach:
- Use two pointers to maintain a sliding window.
- Use a set to store characters currently present in the window.
- Move the right pointer through the string.
- If the current character is already in the set, move the left pointer
  forward and remove characters until the duplicate is removed.
- Add the current character to the set.
- Calculate the current window length and update the maximum length.

Time Complexity:
- O(n)

Space Complexity:
- O(min(n, character set size))

Author:
- Aryan Singh

Date:
- 10/08/2026
"""

s = "abca"

seen = set()

left = 0
max_length = 0


for right in range(len(s)):

    while s[right] in seen:
        seen.remove(s[left])
        left += 1

    
    seen.add(s[right])
        

    current_length = right - left + 1   
    max_length = max(max_length,current_length)

print(max_length)