"""
Problem: Left Rotate Array by One Position
Topic: Arrays
Time Complexity: O(n)
Space Complexity: O(1)
Author: Aryan Singh
Date: 14/07/2026
"""


arr = [1,2,3,4,5]

temp = arr[0]

for i in range(len(arr)-1):
    arr[i] = arr[i+1]

arr[len(arr)-1] = temp

print(arr)