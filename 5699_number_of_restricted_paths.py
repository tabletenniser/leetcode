'''
There is an undirected weighted connected graph. You are given a positive integer n which denotes that the graph has n nodes labeled from 1 to n, and an array edges where each edges[i] = [ui, vi, weighti] denotes that there is an edge between nodes ui and vi with weight equal to weighti.

A path from node start to node end is a sequence of nodes [z0, z1, z2, ..., zk] such that z0 = start and zk = end and there is an edge between zi and zi+1 where 0 <= i <= k-1.

The distance of a path is the sum of the weights on the edges of the path. Let distanceToLastNode(x) denote the shortest distance of a path between node n and node x. A restricted path is a path that also satisfies that distanceToLastNode(zi) > distanceToLastNode(zi+1) where 0 <= i <= k-1.

Return the number of restricted paths from node 1 to node n. Since that number may be too large, return it modulo 109 + 7.

Example 1:
Input: n = 5, edges = [[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]]
Output: 3
Explanation: Each circle contains the node number in black and its distanceToLastNode value in blue. The three restricted paths are:
1) 1 --> 2 --> 5
2) 1 --> 2 --> 3 --> 5
3) 1 --> 3 --> 5
Example 2:

Input: n = 7, edges = [[1,3,1],[4,1,2],[7,3,4],[2,5,3],[5,6,1],[6,7,2],[7,5,3],[2,6,4]]
Output: 1
Explanation: Each circle contains the node number in black and its distanceToLastNode value in blue. The only restricted path is 1 --> 3 --> 7.

Constraints:

1 <= n <= 2 * 104
n - 1 <= edges.length <= 4 * 104
edges[i].length == 3
1 <= ui, vi <= n
ui != vi
1 <= weighti <= 105
There is at most one edge between any two nodes.
There is at least one path between any two nodes.
'''
from collections import defaultdict
from heapq import heappush, heappop
import random

class Solution:
    def dfs(self, node, traversed):
        if node in self.ht:
            return self.ht[node]
        if node == self.target:
            return 1
        cur_dtl = self.dtl[node]
        res = 0
        for new_n, _ in self.graph[node]:
            new_dtl = self.dtl[new_n]
            if new_dtl < cur_dtl:
                traversed.add(new_n)
                res += self.dfs(new_n, traversed)
                traversed.remove(new_n)
        self.ht[node] = res
        return res
    def countRestrictedPaths(self, n, edges) -> int:
        self.ht = {}
        self.target = n
        graph = defaultdict(list)
        for s, e, w in edges:
            graph[s].append((e, w))
            graph[e].append((s, w))
        # print(graph)
        dtl = {}
        q = [(0, n)]
        while len(q) > 0:
            cur_w, cur_n = heappop(q)
            if cur_n in dtl:
                continue
            #print(cur_n, cur_w)
            dtl[cur_n] = min(cur_w, dtl.get(cur_n, 99999999999))
            for next_node, weight in graph[cur_n]:
                if next_node not in dtl:
                    heappush(q, (cur_w+weight, next_node))
        # print(dtl)
        self.graph = graph
        self.dtl = dtl
        return self.dfs(1, set()) % 1000000007

s = Solution()
n = 300
edges = [[i, i+j, random.randint(1, 100000)] for i in range(200) for j in range(200)]
n = 5
edges = [[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]]
n = 7
edges = [[1,3,1],[4,1,2],[7,3,4],[2,5,3],[5,6,1],[6,7,2],[7,5,3],[2,6,4]]
print(s.countRestrictedPaths(n, edges))
