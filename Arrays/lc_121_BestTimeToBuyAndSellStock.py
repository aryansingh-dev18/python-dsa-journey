"""
Problem: LeetCode 121 - Best Time to Buy and Sell Stock

Topic:
- Arrays
- Greedy
- One Pass

Approach:
- Store the first price as the minimum buying price.
- Traverse the array from the second element.
- If a smaller price is found, update minPrice.
- Calculate the profit by selling at the current price:
      profit = current price - minPrice
- Update maxProfit with the maximum profit found so far.

Example:
Input:
[7,3,9,3,8,4]

Best transaction:
Buy at 3
Sell at 9

Maximum Profit:
6

Time Complexity:
- O(n)

Space Complexity:
- O(1)
"""



class Solution:

    def maxProfit(self,prices):

        minPrice = prices[0]
        maxProfit = 0

        for i in range(1,len(prices)):

            if prices[i] < minPrice:
                minPrice = prices[i]

            profit = prices[i] - minPrice
            maxProfit = max(maxProfit,profit)

        return maxProfit

obj = Solution()
print(obj.maxProfit([7,1,5,3,6,4]))
    