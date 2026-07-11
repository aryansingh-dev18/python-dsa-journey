"""
Problem: LeetCode 1929 - Concatenation of Array
Topic: Arrays
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(n)
Author: Aryan Singh
Date: 11/07/2026
"""

nums = [1, 2, 1]
ans = []

# for i in range(len(nums)):
#     ans.append(nums[i])

# for i in range(len(nums)):
#     ans.append(nums[i])

for i in range(2 * len(nums)):
    ans.append(nums[i % len(nums)])

print(ans)