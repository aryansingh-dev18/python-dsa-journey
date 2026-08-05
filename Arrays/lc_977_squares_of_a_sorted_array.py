"""
Problem: LeetCode 977 - Squares of a Sorted Array

Topic:
- Two Pointers

Difficulty:
- Easy

Approach:
- Use two pointers at both ends of the sorted array.
- Compare the absolute values at both ends.
- Place the larger square at the end of the answer array.
- Move the corresponding pointer.
- Continue until all elements are processed.

Time Complexity:
- O(n)

Space Complexity:
- O(n)

Author:
- Aryan Singh

Date:
- 05/08/2026
"""


nums = [-4, -1, 0, 3, 10]

ans = [0]* len(nums)

left = 0
right = len(nums)-1
index = 4

while left <= right:

    if abs(nums[left]) > abs(nums[right]):
        
        ans[index] = nums[left]*nums[left]
        left += 1
        index -= 1

    elif abs(nums[left]) < abs(nums[right]):
    
        ans[index] = nums[right]*nums[right]
        right -= 1
        index -= 1

    else:
        ans[index] = nums[right]*nums[right]
        right -= 1
        index -= 1
        

print(ans)