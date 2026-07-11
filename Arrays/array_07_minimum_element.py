"""
Problem: Minimum element Element
Topic: Arrays
Time Complexity: O(n)
Space Complexity: O(1)
Date: 11 / 07/ 2026
"""

# arr =[12,45,3,67,8,23,2,5]
arr = [-10, -5, -30, -2]
minimum_element = arr[0]

for i in range(1,len(arr)):
    if minimum_element > arr[i]:
        minimum_element = arr[i]
print("Minimum element is ",minimum_element)