"""
Problem: LeetCode 217 - Contains Duplicate

Topic:
- Arrays
- Hash Set

Approach:
- Create an empty set to store elements already seen.
- Traverse the array.
- If the current element already exists in the set, a duplicate is found.
- Return True immediately.
- Otherwise, add the current element to the set.
- If the complete array is traversed without finding a duplicate, return False.

Example:
nums = [1, 2, 3, 1]

Output:
True

Time Complexity:
- O(n)

Space Complexity:
- O(n)
"""

class Solution:

    def containsDuplicate(self,nums):
        seen = set()

        for num  in nums:

            if num in seen:
                return True
            
            else:
                seen.add(num)

        return False


obj = Solution()

print(obj.containsDuplicate([1,2,3,1]))


