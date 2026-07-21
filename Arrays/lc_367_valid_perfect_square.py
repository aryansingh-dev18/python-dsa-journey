"""
Problem: LeetCode 367 - Valid Perfect Square

Topic:
- Binary Search

Difficulty:
- Easy

Approach:
- Apply Binary Search on the search space from 0 to num.
- Compare mid * mid with num.
- If equal, return True.
- If mid * mid is greater than num, search the left half.
- Otherwise, search the right half.
- If the loop finishes without finding an exact square root,
  return False.

Time Complexity:
- O(log n)

Space Complexity:
- O(1)

Author:
- Aryan Singh

Date:
- 21/07/2026
"""

x = 12

left = 0
right = x

while left <= right:
    mid = (left + right) // 2

    if mid*mid == x:
        print(True)
        break
    
    elif mid*mid > x:
        right = mid -1
    
    else:
        left = mid+1

else:
    print(False)