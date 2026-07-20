"""
Problem: LeetCode 35 - Search Insert Position
Topic: Binary Search
Difficulty: Easy
Time Complexity: O(log n)
Space Complexity: O(1)
Author: Aryan Singh
Date: 20/07/2026
"""

arr = [1,3,5,6]
target = 2

left = 0
right = len(arr)-1

while left <= right:
    mid  = (left + right) // 2

    if arr[mid] == target:
        print("Found at index ",mid)
        break

    elif target > arr[mid]:
        left = mid + 1

    else:
        right = mid - 1

else:
    print(left)