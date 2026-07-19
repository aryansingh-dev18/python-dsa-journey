"""
Problem: Binary Search
Topic: Searching
Approach: Binary Search
Time Complexity: O(log n)
Space Complexity: O(1)
Author: Aryan Singh
Date: 19/07/2026
"""

arr = [2,4,6,8,10,12,14]
target = 10

left = 0
right = len(arr)-1

while left <= right :
    mid = (left + right) // 2

    if arr[mid] == target:
        print("Found at index", mid)
        break

    elif target > arr[mid] :
        left = mid + 1

    else:
        right = mid - 1

else:
    print("Target not found")

