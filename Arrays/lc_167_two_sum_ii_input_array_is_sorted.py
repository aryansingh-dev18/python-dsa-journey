"""
Problem: LeetCode 167 - Two Sum II - Input Array Is Sorted

Topic:
- Two Pointers

Difficulty:
- Medium

Approach:
- Place one pointer at the beginning and another at the end of the sorted array.
- Calculate the sum of both elements.
- If the sum equals the target, return their 1-based indices.
- If the sum is smaller than the target, move the left pointer to increase the sum.
- If the sum is greater than the target, move the right pointer to decrease the sum.
- Continue until the required pair is found.

Time Complexity:
- O(n)

Space Complexity:
- O(1)

Author:
- Aryan Singh

Date:
- 03/08/2026
"""

numbers = [2,5,11,15]
target = 20

left = 0
right = len(numbers)-1

while left < right:
    current_sum = numbers[left] + numbers[right]

    if current_sum == target:
        print(left+1, right+1)
        break

    elif current_sum > target:
        right -= 1

    else:
        left +=1

else:
    print("Doesn't exist")

    
        
