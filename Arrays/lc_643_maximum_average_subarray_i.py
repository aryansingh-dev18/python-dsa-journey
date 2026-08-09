"""
Problem: LeetCode 643 - Maximum Average Subarray I

Topic:

* Sliding Window

Difficulty:

* Easy

Approach:

* Calculate the sum of the first window of size k.
* Store it as the current sum and maximum sum.
* Slide the window one position at a time.
* Remove the outgoing element and add the incoming element.
* Update the maximum sum after each window.
* Return the maximum sum divided by k.

Time Complexity:

* O(n)

Space Complexity:

* O(1)

Author:

* Aryan Singh

Date:

* 09/08/2026
  """


nums = [1, 12, -5, -6, 50, 3]
k = 4

current_sum = sum(nums[:k])
max_sum = current_sum

for i in range(k,len(nums)):
    current_sum = current_sum -nums[i-k] + nums[i]
    max_sum = max(max_sum, current_sum)

print(max_sum/k)
    
