"""
Problem: count even and odd in array
Topic: Arrays
Time Complexity: O(n)
Space Complexity: O(1)
Author: Aryan Singh
Date: 18/07/2026
"""

arr = [1,2,3,4,5,6,7,8]

even = 0
odd = 0

for i in range(len(arr)):
    if arr[i] % 2 == 0:
        even +=1
    else:
        odd+=1
print("Even = ",even)
print("Odd = ",odd)