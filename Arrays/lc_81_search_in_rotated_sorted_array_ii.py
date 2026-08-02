"""
Problem: LeetCode 81 - Search in Rotated Sorted Array II

Topic:
- Binary Search

Difficulty:
- Medium

Approach:
- Apply Binary Search on the rotated sorted array containing duplicates.
- Compare arr[left], arr[mid], and arr[right].
- If all three values are equal, shrink the search space by moving both pointers:
    left += 1
    right -= 1
- Otherwise, determine which half is sorted.
- Check whether the target lies inside the sorted half.
- Continue Binary Search until the target is found or the search space becomes empty.
- Return True if the target exists; otherwise, return False.

Time Complexity:
- Average Case: O(log n)
- Worst Case: O(n)   # Due to duplicates

Space Complexity:
- O(1)

Author:
- Aryan Singh

Date:
- 02/08/2026
"""


arr = [1,1,1,3,1]
target = 3

left = 0
right = len(arr)-1

while left <= right :
    mid = (left + right) // 2
    
    if arr[mid] == target:
        print(True)
        break

    if arr[left] == arr[mid] == arr[right]:
        left += 1
        right -= 1
    
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
  print(False)


