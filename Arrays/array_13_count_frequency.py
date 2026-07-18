"""
Problem: Count Frequency of Target Element
Topic: Arrays
Approach: Linear Traversal
Time Complexity: O(n)
Space Complexity: O(1)
Author: Aryan Singh
Date: 18/07/2026
"""

arr = [1,2,2,3,2,4,2,55,2,78,32,2,4,2]
target = 2
count = 0

for i in range(len(arr)):
    if arr[i] == target:
        count += 1
print("Frequency = ",count)