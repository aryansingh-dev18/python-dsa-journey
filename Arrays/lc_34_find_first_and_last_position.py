"""
Problem: LeetCode 34 - Find First and Last Position of Element in Sorted Array

Topic:
- Binary Search

Difficulty:
- Medium

Approach:
- Perform Binary Search twice.
- First Binary Search finds the first occurrence of the target.
- Second Binary Search finds the last occurrence of the target.
- If the target is found, store the index and continue searching
  in the required direction to locate the boundary occurrence.

Time Complexity:
- O(log n)

Space Complexity:
- O(1)

Author:
- Aryan Singh

Date:
- 20/07/2026
"""

arr = [5,7,7,8,8,10]
target = 8


left = 0
right = len(arr)-1
first = -1

while left <= right:
    mid  = (left + right) // 2

    if arr[mid] == target:
        first = mid
        right = mid - 1
        
        
    elif target > arr[mid]:
        left = mid + 1

    else:
        right = mid - 1



left = 0
right = len(arr)-1
last = -1

while left <= right:
    mid  = (left + right) // 2

    if arr[mid] == target:
        last = mid
        left = mid + 1
        
        
    elif target > arr[mid]:
        left = mid + 1

    else:
        right = mid - 1

print("First Occurance:",first,",Last Occurance:",last)

    
