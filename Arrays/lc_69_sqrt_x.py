"""
Problem: LeetCode 69 - Sqrt(x)

Topic:
- Binary Search

Difficulty:
- Easy

Approach:
- Apply Binary Search on the search space from 0 to x.
- Compare mid * mid with x.
- If equal, return mid.
- If mid * mid is greater than x, search the left half.
- Otherwise, search the right half.
- If no exact square root exists, return the last valid value (right).

Time Complexity:
- O(log x)

Space Complexity:
- O(1)

Author:
- Aryan Singh

Date:
- 21/07/2026
"""

x = 20

left = 0
right = x

while left <= right:
    mid  = (left + right) // 2

    if mid*mid == x:
        print(mid)
        break

    elif mid*mid > x:
        right = mid - 1

    else:
        left = mid + 1

else:
    print(right)