"""
Problem: LeetCode 283 - Move Zeroes
Topic: Arrays, Two Pointers
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)
Author: Aryan Singh
Date: 18/07/2026
"""

nums = [0,1,0,3,1,0,2]

j = 0

for i in range(len(nums)):
    if nums[i] != 0:
        nums[i] , nums[j] = nums[j],nums[i]
        j += 1
print(nums)

