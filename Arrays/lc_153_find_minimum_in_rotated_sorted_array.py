"""
Problem: LeetCode 153 - Find Minimum in Rotated Sorted Array

Topic:
- Binary Search

Difficulty:
- Medium

Approach:
- Apply Binary Search on the rotated sorted array.
- Compare arr[mid] with arr[right].
- If arr[mid] > arr[right], the minimum lies in the right half.
- Otherwise, the minimum lies in the left half including mid.
- Continue until left == right.
- Return the minimum element.

Time Complexity:
- O(log n)

Space Complexity:
- O(1)

Author:
- Aryan Singh

Date:
- 03/08/2026
"""


arr = [3,4,5,1,2]

left = 0
right = len(arr)-1

while left < right:
    mid = (left + right) // 2


    if arr[mid] > arr[right]:
        left = mid + 1

    else:
        right = mid

print(arr[left])

    