'''
You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].
The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.
Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

Example 1:
Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
Explanation:
We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.

Example 2:
Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18

Example 3:
Input: points = [[0,0],[1,1],[1,0],[-1,1]]
Output: 4

Example 4:
Input: points = [[-1000000,-1000000],[1000000,1000000]]
Output: 4000000

Example 5:
Input: points = [[0,0]]
Output: 0

Constraints:
1 <= points.length <= 1000
-106 <= xi, yi <= 106
All pairs (xi, yi) are distinct.
'''
from collections import defaultdict
import heapq
class Solution:
    def minCostConnectPoints(self, points) -> int:
        edges = defaultdict(list)
        n = len(points)
        connected_pts = set([0])
        pending_edges = []
        for i in range(n):
            for j in range(i+1,n):
                w = abs(points[j][1] - points[i][1]) + abs(points[j][0] - points[i][0])
                edges[i].append((w, j))
                edges[j].append((w, i))
        # print(edges)
        for e in edges[0]:
            heapq.heappush(pending_edges, (e[0], e[1]))
            # pending_edges.append((e[0], e[1]))

        res = 0
        while len(connected_pts) < n:
            # pending_edges.sort()
            # print(pending_edges)
            found_edge = False
            while not found_edge:
                e = heapq.heappop(pending_edges)
                if e[1] in connected_pts:
                    continue
                found_edge = True
                connected_pts.add(e[1])
                res += e[0]
                for next_edge in edges[e[1]]:
                    if next_edge not in connected_pts:
                        heapq.heappush(pending_edges, (next_edge[0], next_edge[1]))
                        # pending_edges.append((next_edge[0], next_edge[1]))
        return res


points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
points = [[3,12],[-2,5],[-4,1]]
points = [[0,0]]
points = [[0,0],[1,1],[1,0],[-1,1]]
points = [[i,i] for i in range(800)]
sol = Solution()
print(sol.minCostConnectPoints(points))
