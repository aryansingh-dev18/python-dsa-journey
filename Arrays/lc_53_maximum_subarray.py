"""
Problem: LeetCode 53 - Maximum Subarray

Topic:
- Arrays
- Kadane's Algorithm
- Greedy

Approach:
- Initialize current_sum and max_sum with the first element.
- Traverse the array from the second element.
- For every element, decide whether to:
  1. Continue the current subarray.
  2. Start a new subarray from the current element.
- Store the larger value in current_sum.
- Update max_sum with the maximum sum found so far.
- Return max_sum.

Example:
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

Maximum Subarray:
[4, -1, 2, 1]

Output:
6

Time Complexity:
- O(n)

Space Complexity:
- O(1)
"""

class Solution:
    def maxSubArray(self, nums):
        current_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(max_sum, current_sum)

        return max_sum


obj = Solution()

print(obj.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))