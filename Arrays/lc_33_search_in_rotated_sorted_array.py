"""
Problem: LeetCode 33 - Search in Rotated Sorted Array

Topic:
- Binary Search

Difficulty:
- Medium

Approach:
- Apply Binary Search on the rotated sorted array.
- Find which half of the array is sorted.
- Check whether the target lies inside the sorted half.
- Search only in the half where the target can exist.
- If the target is found, return its index.
- Otherwise, return -1.

Time Complexity:
- O(log n)

Space Complexity:
- O(1)

Author:
- Aryan Singh

Date:
- 28/07/2026
"""

arr = [4,5,6,7,0,1,2]
target = 0

left = 0
right = len(arr) - 1

while left <= right:
    mid = (left + right) // 2

    if arr[mid] == target:
        print(mid)
        break

    elif arr[left] <= arr[mid]:

        if arr[left] <= target <= arr[mid]:
            right = mid -1
            
        else:
            left = mid + 1

    else:

        if arr[mid] <= target <= arr[right]:
            left = mid + 1

        else:
            right = mid - 1

else:
    print("-1")
        

