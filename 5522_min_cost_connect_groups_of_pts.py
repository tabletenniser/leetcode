'''
You are given two groups of points where the first group has size1 points, the second group has size2 points, and size1 >= size2.
The cost of the connection between any two points are given in an size1 x size2 matrix where cost[i][j] is the cost of connecting point i of the first group and point j of the second group. The groups are connected if each point in both groups is connected to one or more points in the opposite group. In other words, each point in the first group must be connected to at least one point in the second group, and each point in the second group must be connected to at least one point in the first group.
Return the minimum cost it takes to connect the two groups.

Example 1:
Input: cost = [[15, 96], [36, 2]]
Output: 17
Explanation: The optimal way of connecting the groups is:
1--A
2--B
This results in a total cost of 17.

Example 2:
Input: cost = [[1, 3, 5], [4, 1, 1], [1, 5, 3]]
Output: 4
Explanation: The optimal way of connecting the groups is:
1--A
2--B
2--C
3--A
This results in a total cost of 4.
Note that there are multiple points connected to point 2 in the first group and point A in the second group. This does not matter as there is no limit to the number of points that can be connected. We only care about the minimum total cost.

Example 3:
Input: cost = [[2, 5, 1], [3, 4, 7], [8, 1, 2], [6, 2, 4], [3, 8, 8]]
Output: 10

Constraints:
size1 == cost.length
size2 == cost[i].length
1 <= size1, size2 <= 12
size1 >= size2
0 <= cost[i][j] <= 100
'''
from functools import lru_cache
class Solution:
    def connectTwoGroups(self, cost) -> int:
        m, n = len(cost), len(cost[0])
        min_arr = [min(x) for x in zip(*cost)]

        # @lru_cache(None)
        def dp(i, mask):
            print(i,mask)
            if i == m:
                ans = 0
                for j in range(n):
                    if not mask & (1 << j):
                        ans += min_arr[j]
                return ans

            ans = float('inf')
            for j in range(n):
                ans = min(ans, cost[i][j] + dp(i + 1, mask | (1 << j)))
            return ans

        return dp(0, 0)

    def connectTwoGroups2(self, cost) -> int:
        res = 0
        cur_sinks = dict()
        for row in cost:
            min_c = min(row)
            res += min_c
            cur_sinks[row.index(min_c)] = cur_sinks.get(row.index(min_c), 0) + 1
        print(cur_sinks)
        min_addition = 999999999
        for sink_i in range(len(cost[0])):
            if sink_i not in cur_sinks:
                res += [min(i) for i in zip(*cost)][sink_i]
        return res

cost = [[15, 96], [36, 2]]
# cost = [[1, 3, 5], [4, 1, 1], [1, 5, 3]]
# cost = [[2, 5, 1], [3, 4, 7], [8, 1, 2], [6, 2, 4], [3, 8, 8]]
# cost = [[93,56,92],[53,44,18],[86,44,69],[54,60,30]]
s = Solution()
print(s.connectTwoGroups(cost))
