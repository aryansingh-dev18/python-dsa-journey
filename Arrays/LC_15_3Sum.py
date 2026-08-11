"""
Problem: LeetCode 15 - 3Sum

Topic:
- Arrays
- Sorting
- Two Pointers

Difficulty:
- Medium

Approach:
- Sort the given array first.
- Use one pointer (i) to fix the first element of the triplet.
- Use two pointers (left and right) to find the other two elements.
- If the total sum is less than 0, move left forward to increase the sum.
- If the total sum is greater than 0, move right backward to decrease the sum.
- If the total sum is 0, store the triplet in the answer.
- Skip duplicate values for i, left, and right to avoid duplicate triplets.

Time Complexity:
- O(n^2)

Space Complexity:
- O(1) auxiliary space
  (excluding the output array)

Author:
- Aryan Singh

Date:
- 11/08/2026
"""

nums = [-1, 0, 1, 2, -1, -4]

nums.sort()

ans = []

for i in range(len(nums)):

    if i>0 and nums[i] == nums[i-1]:
        continue

    left = i + 1
    right = len(nums) - 1

    while left < right:

        total = nums[i] + nums[left] + nums[right]

        if  total < 0 :
            left += 1

        elif total > 0 :
            right -= 1

        else:
            ans.append([nums[i], nums[left], nums[right]])
            left += 1
            right -= 1

            while left < right and nums[left] == nums[left-1]:
             left += 1

            while left < right and nums[right] == nums[right+1]:
                right -= 1
        
print(ans)
