"""
Problem: LeetCode 169 - Majority Element

Topic:
- Arrays
- Hash Map
- Frequency Counting

Approach:
- Create a dictionary to store the frequency of each element.
- Traverse the array and update the frequency of every number.
- After updating the frequency, check whether the current number appears
  more than n/2 times.
- If it does, return that number immediately.

Example:
nums = [1, 3, 2, 4, 2, 2, 2, 2]

Output:
2

Time Complexity:
- O(n)

Space Complexity:
- O(n)
"""

class Solution:
    def majorityElement(self,nums):
        freq = {}
        
        for num in nums:

            if num in freq:
                freq[num] += 1

            else:
                freq[num] = 1

            if freq[num] > len(nums)//2 :
                return num

obj = Solution()

print(obj.majorityElement([1,3,2,4,2,2,2,2]))
