"""
You have two fruit baskets containing n fruits each. You are given two 0-indexed integer arrays basket1 and basket2 representing the cost of fruit in each basket. You want to make both baskets equal. To do so, you can use the following operation as many times as you want:
Chose two indices i and j, and swap the ith fruit of basket1 with the jth fruit of basket2.
The cost of the swap is min(basket1[i],basket2[j]).
Two baskets are considered equal if sorting them according to the fruit cost makes them exactly the same baskets.
Return the minimum cost to make both the baskets equal or -1 if impossible.

Example 1:
Input: basket1 = [4,2,2,2], basket2 = [1,4,1,2]
Output: 1
Explanation: Swap index 1 of basket1 with index 0 of basket2, which has cost 1. Now basket1 = [4,1,2,2] and basket2 = [2,4,1,2]. Rearranging both the arrays makes them equal.
Example 2:

Input: basket1 = [2,3,4,1], basket2 = [3,2,5,1]
Output: -1
Explanation: It can be shown that it is impossible to make both the baskets equal.

Constraints:
basket1.length == bakste2.length
1 <= basket1.length <= 105
1 <= basket1[i],basket2[i] <= 109
"""

from collections import Counter
class Solution:
    def minCost(self, basket1, basket2) -> int:
        c1 = Counter(basket1)
        c2 = Counter(basket2)
        c = c1 + c2
        # print(sorted(basket1))
        # print(sorted(basket2))
        # print(c1, c2, c)
        cost = []
        balance = 0
        for k in c:
            if c[k] % 2 == 1:
                return -1
            balance += c1[k] - c2[k]
            diff = abs(c1[k] - c2[k])
            assert diff % 2 == 0
            if diff > 0:
                cost.extend([k] * (diff // 2))
        if balance != 0:
            return -1
        cost.sort()
        # print(cost)
        min_k = min(c.keys())
        res = 0
        for c in cost[:len(cost) // 2]:
            res += min(c, min_k*2)
        return res

s = Solution()
# basket1 = [4,2,2,2]
# basket2 = [1,4,1,2]
# print(s.minCost(basket1, basket2))
# basket1 = [2,3,4,1]
# basket2 = [3,2,5,1]
# print(s.minCost(basket1, basket2))
# basket1 = [4,4,4,4,3]
# basket2 = [5,5,5,5,3]
# print(s.minCost(basket1, basket2))
basket1 = [84,80,43,8,80,88,43,14,100,88]
basket2 = [32,32,42,68,68,100,42,84,14,8]
print(s.minCost(basket1, basket2))
