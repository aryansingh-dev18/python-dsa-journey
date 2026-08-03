"""
Problem: LeetCode 154 - Find Minimum in Rotated Sorted Array II

Topic:
- Binary Search

Difficulty:
- Hard

Approach:
- Apply Binary Search on the rotated sorted array containing duplicates.
- Compare arr[mid] with arr[right].
- If arr[mid] > arr[right], the minimum lies in the right half.
- If arr[mid] < arr[right], the minimum lies in the left half including mid.
- If arr[mid] == arr[right], shrink the search space by reducing right.
- Continue until left == right.
- Return the minimum element.

Time Complexity:
- Average Case: O(log n)
- Worst Case: O(n)   # Due to duplicates

Space Complexity:
- O(1)

Author:
- Aryan Singh

Date:
- 03/08/2026
"""

arr = [1,1,1,0,1]

left = 0
right = len(arr)-1

while left < right:
    mid = (left + right) // 2

    if arr[mid] > arr[right]:
        left = mid+1

    elif arr[mid] < arr[right]:
        right = mid

    else:
        right -=1

print(arr[left])
