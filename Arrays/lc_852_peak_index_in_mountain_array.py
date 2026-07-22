"""
Problem: LeetCode 852 - Peak Index in a Mountain Array

Topic:
- Binary Search

Difficulty:
- Easy

Approach:
- Apply Binary Search on the mountain array.
- Compare arr[mid] with arr[mid + 1].
- If arr[mid] < arr[mid + 1], move to the right half.
- Otherwise, move to the left half including mid.
- When left == right, it points to the peak index.

Time Complexity:
- O(log n)

Space Complexity:
- O(1)

Author:
- Aryan Singh

Date:
- 22/07/2026
"""


arr = [0,2,5,6,8,7,3]

left = 0
right = len(arr)-1

while left < right :
    mid = (left + right) // 2

    if arr[mid] < arr[mid + 1] :
        left = mid + 1

    else:
        right = mid 
    
print(left)