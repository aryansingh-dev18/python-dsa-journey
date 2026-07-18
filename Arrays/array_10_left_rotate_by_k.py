"""
Problem: Left Rotate Array by K Positions
Topic: Arrays
Approach: Repeated Left Rotation
Time Complexity: O(n × k)
Space Complexity: O(1)
Author: Aryan Singh
Date: 18/07/2026
"""

arr = [1,2,3,4,5]
k = 2

for _ in range(k):
    temp = arr[0]
    for i in range(len(arr)-1):
        arr[i] = arr[i+1]

    arr[len(arr)-1] = temp

print(arr)