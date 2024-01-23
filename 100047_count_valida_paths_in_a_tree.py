"""
There is an undirected tree with n nodes labeled from 1 to n. You are given the integer n and a 2D integer array edges of length n - 1, where edges[i] = [ui, vi] indicates that there is an edge between nodes ui and vi in the tree.
Return the number of valid paths in the tree.
A path (a, b) is valid if there exists exactly one prime number among the node labels in the path from a to b.

Note that:
The path (a, b) is a sequence of distinct nodes starting with node a and ending with node b such that every two adjacent nodes in the sequence share an edge in the tree.
Path (a, b) and path (b, a) are considered the same and counted only once.

Example 1:
Input: n = 5, edges = [[1,2],[1,3],[2,4],[2,5]]
Output: 4
Explanation: The pairs with exactly one prime number on the path between them are: 
- (1, 2) since the path from 1 to 2 contains prime number 2. 
- (1, 3) since the path from 1 to 3 contains prime number 3.
- (1, 4) since the path from 1 to 4 contains prime number 2.
- (2, 4) since the path from 2 to 4 contains prime number 2.
It can be shown that there are only 4 valid paths.
Example 2:
Input: n = 6, edges = [[1,2],[1,3],[2,4],[3,5],[3,6]]
Output: 6
Explanation: The pairs with exactly one prime number on the path between them are: 
- (1, 2) since the path from 1 to 2 contains prime number 2.
- (1, 3) since the path from 1 to 3 contains prime number 3.
- (1, 4) since the path from 1 to 4 contains prime number 2.
- (1, 6) since the path from 1 to 6 contains prime number 3.
- (2, 4) since the path from 2 to 4 contains prime number 2.
- (3, 6) since the path from 3 to 6 contains prime number 3.
It can be shown that there are only 6 valid paths.

Constraints:
1 <= n <= 105
edges.length == n - 1
edges[i].length == 2
1 <= ui, vi <= n
The input is generated such that edges represent a valid tree.
"""
class Solution:
    def get_prime_numbers_below_n(self, n):
        prime_numbers = [2]
        for i in range(3, n+1, 2):
            is_prime = True
            for j in prime_numbers:
                if j*j > i:
                    break
                if i%j == 0:
                    is_prime = False
                    break
            if is_prime:
                prime_numbers.append(i)
        return prime_numbers
    def countPaths(self, n: int, edges) -> int:
        adjancy_graph = {}
        for edge in edges:
            if edge[0] not in adjancy_graph:
                adjancy_graph[edge[0]] = []
            if edge[1] not in adjancy_graph:
                adjancy_graph[edge[1]] = []
            adjancy_graph[edge[0]].append(edge[1])
            adjancy_graph[edge[1]].append(edge[0])
        print(adjancy_graph)
        prime_numbers_below_n = self.get_prime_numbers_below_n(100000)
        count_map = {}
        for p in prime_numbers_below_n:
            if p > n:
                break
            visited = set()
            def dfs(node, cm, is_first_layer):
                nonlocal visited
                # print(node, adjancy_graph[node], res)
                visited.add(node)
                r = 0 if is_first_layer else 1
                for child in adjancy_graph[node]:
                    if child not in visited and child not in prime_numbers_below_n:
                        dfs_r = dfs(child, cm, False)
                        # print(node, child, r, dfs_r)
                        if is_first_layer:
                            if node in cm:
                                cm[node].append(dfs_r)
                            else:
                                cm[node] = [dfs_r]
                        else:
                            r += dfs_r
                return r

            dfs(p, count_map, True)
        print(count_map)
        res = 0
        for k, v in count_map.items():
            if len(v) == 1:
                res += v[0]
            else:
                for i in range(len(v)):
                    for j in range(i+1, len(v)):
                        res += (v[i] + 1) * v[j] + v[i]
        return res


s = Solution()
print(s.countPaths(n = 9, edges = [[7,4],[3,4],[5,4],[1,5],[6,4],[9,5],[8,7],[2,8]]))
# print(s.countPaths(n = 5, edges = [[1,2],[1,3],[2,4],[2,5]]))
# print(s.countPaths(n = 6, edges = [[1,2],[1,3],[2,4],[3,5],[3,6]]))
