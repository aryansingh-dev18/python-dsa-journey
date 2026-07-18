"""
Problem: Find Missing Number in Array
Topic: Arrays
Approach: Linear Search
Time Complexity: O(n²)
Space Complexity: O(1)
Author: Aryan Singh
Date: 18/07/2026
"""

arr = [1,2,3,5]

for num in range(1, len(arr)+2):
    found = False   
    for i in range(len(arr)):
        if arr[i] == num:
            found = True
            break
    if not found:
        print(num)
        break

