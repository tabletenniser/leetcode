'''
Your are given an array of integers prices, for which the i-th element is the price of a given stock on day i; and a non-negative integer fee representing a transaction fee.

You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction. You may not buy more than 1 share of a stock at a time (ie. you must sell the stock share before you buy again.)

Return the maximum profit you can make.

Example 1:
Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
Buying at prices[0] = 1
Selling at prices[3] = 8
Buying at prices[4] = 4
Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
Note:

0 < prices.length <= 50000.
0 < prices[i] < 50000.
0 <= fee < 50000.
'''
class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        result = 0
        prev_purchase = 9999999999
        prev_sell = prev_purchase
        purchase = prev_purchase
        for p in prices:
            # Sell at this price instead
            if p > prev_sell and purchase>prev_purchase+2:
                print p,prev_purchase,prev_sell
                result -= prev_sell - prev_purchase - 2
                result += p - prev_purchase - 2
                # result += p - prev_sell
                prev_sell = p
            # Let's try selling it
            elif p - purchase - 2 > 0:
                # Unwind prev_purchase
                if p - prev_purchase - 2 > (prev_sell-prev_purchase-2) + (p - purchase-2):
                    result -= prev_sell - prev_purchase - 2
                    result += p-prev_purchase-2
                else:
                    result += p - purchase - 2
                prev_purchase = purchase
                prev_sell = p
                purchase = 99999999999
            purchase = min(purchase, p)
        return result

s = Solution()
print s.maxProfit([1,3,2,8], 2) # (8-1-2)=5
print s.maxProfit([1,5,2,8], 2) # (8-2-2)+(5-1+2)=6
print s.maxProfit([1,6,5,8], 2) # 5
print s.maxProfit([1,10,5,8], 2) # 7+1
print s.maxProfit([1,5,6,2,8], 2) # (6-1-2)+(8-2-2) = 7
