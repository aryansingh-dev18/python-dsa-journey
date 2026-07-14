
"""
Problem: LeetCode 1480 - Running Sum of 1D Array
Topic: Arrays
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)
Author: Aryan Singh
Date: 14/07/2026
"""

nums = [1,2,3,4]

for i in range(1,len(nums)):
    nums[i]  = nums[i] + nums[i-1]

print(nums)

