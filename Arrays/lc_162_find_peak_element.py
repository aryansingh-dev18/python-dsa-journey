"""
Problem: LeetCode 162 - Find Peak Element

Topic:
- Binary Search

Difficulty:
- Medium

Approach:
- Apply Binary Search on the array.
- Compare arr[mid] with arr[mid + 1].
- If arr[mid] < arr[mid + 1], move to the right half.
- Otherwise, move to the left half including mid.
- Continue until left == right.
- The final position of left (or right) is the index of a peak element.

Time Complexity:
- O(log n)

Space Complexity:
- O(1)

Author:
- Aryan Singh

Date:
- 28/07/2026
"""

arr = [1,2,1,3,5,6,4]

left = 0
right = len(arr)-1

while left < right:
    mid =  (left + right) // 2

    if arr[mid] < arr[mid+1]:
        left = mid + 1

    else:
        right = mid

print(left)