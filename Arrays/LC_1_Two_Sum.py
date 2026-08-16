"""
Problem: LeetCode 1 - Two Sum

Topic:
- Arrays
- Hash Map
- Complement Technique

Approach:
- Create a dictionary to store each number and its index.
- Traverse the array from left to right.
- For every element, calculate its complement:
      complement = target - nums[i]
- Check whether the complement already exists in the dictionary.
- If it exists, return the stored index of the complement and the current index.
- If it does not exist, store the current number and its index.
- This avoids using two nested loops.

Example:
nums = [2, 7, 11, 15]
target = 9

Output:
[0, 1]

Time Complexity:
- O(n)

Space Complexity:
- O(n)
"""

class Solution:
    def twoSum(self, nums, target):
        seen = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in seen:
                return [seen[complement], i]

            else:
                seen[nums[i]] = i


obj = Solution()

print(obj.twoSum([2, 7, 11, 15], 17))