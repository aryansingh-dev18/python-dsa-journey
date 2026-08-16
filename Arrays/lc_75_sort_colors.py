"""
Problem: LeetCode 75 - Sort Colors

Topic:
- Arrays
- Two Pointers
- Three Pointers
- Dutch National Flag Algorithm

Approach:
- Use three pointers: low, mid, and high.
- low represents the position where the next 0 should be placed.
- mid is used to scan the current element.
- high represents the position where the next 2 should be placed.

Rules:
- If nums[mid] == 0:
    Swap nums[low] and nums[mid].
    Increment low and mid.

- If nums[mid] == 1:
    1 is already in the correct middle section.
    Increment mid only.

- If nums[mid] == 2:
    Swap nums[mid] and nums[high].
    Decrement high.
    Do not increment mid because the swapped element
    still needs to be checked.

Example:
nums = [2, 0, 2, 1, 1, 0]

Output:
[0, 0, 1, 1, 2, 2]

Time Complexity:
- O(n)

Space Complexity:
- O(1)
"""

class Solution:
    def sortColors(self,nums):
        low = 0
        mid = 0
        high = len(nums)-1

        while mid <= high:

            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1

            elif nums[mid] == 1:
                mid+=1

            else:
                nums[mid] , nums[high] = nums[high],nums[mid]
                high -= 1

        return nums

obj = Solution()
print(obj.sortColors([2,0,2,1,1,0]))