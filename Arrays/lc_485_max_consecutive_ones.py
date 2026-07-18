"""
Problem: LeetCode 485 - Max Consecutive Ones
Topic: Arrays
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)
Author: Aryan Singh
Date: 18/07/2026
"""

nums = [1,1,1,1,0,1,1,1]

count = 0
maximum = 0

for i in range (len(nums)):
    if nums[i] == 1:
        count += 1
        maximum = max(maximum , count)
    else:
        count = 0
print(maximum)

