"""
Problem: LeetCode 238 - Product of Array Except Self

Topic:
- Arrays
- Prefix Product
- Suffix Product

Approach:
- Create an answer array initialized with 1.
- First pass from left to right:
    Store the product of all elements to the left of each index.
- Second pass from right to left:
    Multiply each answer value by the product of all elements
    to the right.
- This gives the product of all elements except the current element.
- Division is not used.

Example:
Input:
[1,2,3,4]

Output:
[24,12,8,6]

Time Complexity:
- O(n)

Space Complexity:
- O(1) extra space
  (excluding the output array)
"""

class Solution:
    def productExceptSelf(self,nums):

        ans = [1]*len(nums)

        prefix = 1

        for i in range(len(nums)):
            ans[i] = prefix
            prefix *= nums[i]

        suffix = 1

        for i in range(len(nums) -1,-1, -1):
            ans[i] *= suffix
            suffix *= nums[i] 

        return ans

obj = Solution()
print(obj.productExceptSelf([1,2,3,4]))
