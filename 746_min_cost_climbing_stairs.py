'''
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

Example 1:
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
Example 2:
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
Note:
cost will have a length in the range [2, 1000].
Every cost[i] will be an integer in the range [0, 999].
'''
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        def rec(cost, cache):
            if tuple(cost) in cache:
                return cache[tuple(cost)]
            if len(cost) <= 1:
                return 0
            elif len(cost) == 2:
                return min(cost[1], cost[0])
            new_cost = min(rec(cost[1:], cache) + cost[0],
                rec(cost[2:], cache) + cost[1])
            cache[tuple(cost)] = new_cost
            return new_cost

        hash_table = dict()
        return rec(cost, hash_table)

s = Solution()
print s.minCostClimbingStairs([10, 15, 20])
print s.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
