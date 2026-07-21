"""
Problem: LeetCode 374 - Guess Number Higher or Lower

Topic:
- Binary Search

Difficulty:
- Easy

Approach:
- Apply Binary Search on the search space from 1 to n.
- Use the guess() API to determine whether the current guess
  is too high, too low, or correct.
- If the guess is too low, search the right half.
- If the guess is too high, search the left half.
- Stop when the correct number is found.

Time Complexity:
- O(log n)

Space Complexity:
- O(1)

Author:
- Aryan Singh

Date:
- 21/07/2026


"""


n = 100
secret = 500




def guess(num):

    if num == secret:
        return 0
    elif num < secret:
        return 1
    else:
        return -1
    

left = 1
right = n

while left <= right:
    mid = (left + right) // 2

    result = guess(mid) 
    
    if result == 0:
        print(mid)
        break
            
    elif result == 1:
        left = mid + 1
            
    else:
        right = mid - 1

else:
    print("Secret number is not within the range 1 to", n)




