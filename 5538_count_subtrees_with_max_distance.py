'''
There are n cities numbered from 1 to n. You are given an array edges of size n-1, where edges[i] = [ui, vi] represents a bidirectional edge between cities ui and vi. There exists a unique path between each pair of cities. In other words, the cities form a tree.

A subtree is a subset of cities where every city is reachable from every other city in the subset, where the path between each pair passes through only the cities from the subset. Two subtrees are different if there is a city in one subtree that is not present in the other.

For each d from 1 to n-1, find the number of subtrees in which the maximum distance between any two cities in the subtree is equal to d.

Return an array of size n-1 where the dth element (1-indexed) is the number of subtrees in which the maximum distance between any two cities is equal to d.

Notice that the distance between the two cities is the number of edges in the path between them.

Example 1:
Input: n = 4, edges = [[1,2],[2,3],[2,4]]
Output: [3,4,0]
Explanation:
The subtrees with subsets {1,2}, {2,3} and {2,4} have a max distance of 1.
The subtrees with subsets {1,2,3}, {1,2,4}, {2,3,4} and {1,2,3,4} have a max distance of 2.
No subtree has two nodes where the max distance between them is 3.

Example 2:
Input: n = 2, edges = [[1,2]]
Output: [1]

Example 3:
Input: n = 3, edges = [[1,2],[2,3]]
Output: [2,1]

Constraints:
2 <= n <= 15
edges.length == n-1
edges[i].length == 2
1 <= ui, vi <= n
All pairs (ui, vi) are distinct.
'''
from itertools import permutations
class Solution:
    def dfs(self, cur_s, cur_node, cur_d):
        if len(cur_s) == 0:
            cur_d = 0
        if cur_d > 0:
            self.res[cur_d-1].append(cur_s)
        for n in self.adj_list[cur_node]:
            set_with_cur_node = cur_s.union(set[cur_node])
            self.dfs(set_with_cur_node, n, cur_d + 1)
            self.dfs(cur_s, n, cur_d + 1)

    def countSubgraphsForEachDiameter2(self, n: int, edges):
        self.adj_list = [set() for _ in range(n)]
        for f, t in edges:
            a,b = min(f,t)-1, max(f,t) - 1
            self.adj_list[a].add(b)
        print(self.adj_list)
        cur_s = set()
        cur_node = 0
        cur_d = 0
        self.res = [set() for _ in range(n)]
        self.dfs(cur_s, 0, cur_d)
        return self.res

    def dfs(self, node_set, node):
        next_nodes = node_set.intersection(self.adj_list[node])
        if node in node_set:
            node_set.remove(node)
        if len(next_nodes) == 0:
            return 0
        sub_ranks = []
        for next_node in next_nodes:
            sub_ranks.append(self.dfs(node_set, next_node))
        sub_ranks.sort(reverse = True)
        print(node_set,node,sub_ranks)
        if len(sub_ranks) == 1:
            return sub_ranks[0] + 1
        return sub_ranks[0] + sub_ranks[1] + 2

    def calcDist(self, node_list):
        for i in range(len(node_list)):
            for j in range(i+1, len(node_list)):
                dist = self.magic_table[i+1][j+1]
        return -1

    def rec(self, cur_set, cur_n):
        if cur_n == n:
            dist = self.calcDist(list(cur_set))
            print(cur_set, 'is', dist)
            if dist != -1:
                self.res[dist].add(tuple(cur_set))
            return
        self.rec(cur_set, cur_n + 1)
        set_with_cur_node = cur_set.union(set([cur_n]))
        self.rec(set_with_cur_node, cur_n + 1)

    def getTable(self, n, edges):
        g = defaultdict(list)
        for e in edges:
            u, v = e[0], e[1]
            g[u].append(v)
            g[v].append(u)
        tb = [[-1 for i in range(n+1)] for j in range(n+1)]
        cnt = 0
        best = [0 for i in range(n+1)]
        for e in edges:
            u, v = min(e[0], e[1]), max(e[0], e[1])
            tb[u][v] = 1
            best[u] += 1
            best[v] += 1
            cnt += 1
        nxt = best.index(max(best))
        rnd = 2
        while cnt < n * (n-1) // 2:
            L = list(itertools.combinations(g[nxt], 2))
            best = [0 for i in range(n+1)]
            for l in L:
                u, v = min(l[0], l[1]), max(l[0], l[1])
                tb[u][v] = rnd
                best[u] += 1
                best[v] += 1
                cnt += 1
            rnd += 1
            nxt = best.index(max(best))
        return tb

    def countSubgraphsForEachDiameter(self, n: int, edges):
        self.magic_table = self.getTable(n, edges)
        self.n = n
        self.adj_list = [set() for _ in range(n)]
        for f, t in edges:
            a,b = min(f,t)-1, max(f,t) - 1
            self.adj_list[a].add(b)
            self.adj_list[b].add(a)
        cur_set = set()
        self.res = [set() for _ in range(n)]
        self.rec(cur_set, 0)
        return self.res

n = 4
edges = [[1,2],[2,3],[2,4]]
sol = Solution()
print(sol.countSubgraphsForEachDiameter(n, edges))
