"""
Problem: Move All Zeros to End
Topic: Arrays, Two Pointers
Time Complexity: O(n)
Space Complexity: O(1)
Date: 11/07/2026
"""

arr = [0,1,0,3,14,32,0,65,8,9]
j = 0

for i in range(len(arr)):
    if arr[i] != 0:
        arr[i], arr[j] = arr[j] ,arr[i]
        j += 1
print(arr)