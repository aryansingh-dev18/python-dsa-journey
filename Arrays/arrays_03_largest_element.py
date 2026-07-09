"""
Problem: Largest Element
Topic: Arrays
Time Complexity: o(n)
Space Complexity: o(1)
Date: 09 / 07/ 2026
"""

arr = [12, 67, 45, 89, 23]
largest = arr[0]
for i in  range(1,len(arr)):
    if arr[i] > largest:
       largest = arr[i]
print(largest)