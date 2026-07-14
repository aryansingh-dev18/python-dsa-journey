"""
Problem: LeetCode 26 --Remove Duplicate from sorted array
Topic: Arrays
Difficulty: Easy
Time Complexity: O(n)
Space Complexity: O(1)
Author: Aryan Singh
Date: 14/07/2026
"""

arr = [1,1,2,2,3,4,4]
j = 0

for i in range(1,len(arr)):
    if arr[i] != arr[j]:
        j += 1
        arr[j] = arr[i]
print(arr)
print("Unique element =", j + 1)