'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
'''
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        for i in xrange(1, len(prices)):
            max_profit += max(prices[i] - prices[i-1], 0)
        return max_profit


s = Solution()
assert s.maxProfit([1,3,5,6]) == 5
assert s.maxProfit([1,3,2,6]) == 6
assert s.maxProfit([9,3,2,6]) == 4
assert s.maxProfit([]) == 0
assert s.maxProfit([1, 10, 5]) == 9
print "All test passes!"
