'''
Given a tree (i.e. a connected, undirected graph that has no cycles) consisting of n nodes numbered from 0 to n - 1 and exactly n - 1 edges. The root of the tree is the node 0, and each node of the tree has a label which is a lower-case character given in the string labels (i.e. The node with the number i has the label labels[i]).

The edges array is given on the form edges[i] = [ai, bi], which means there is an edge between nodes ai and bi in the tree.

Return an array of size n where ans[i] is the number of nodes in the subtree of the ith node which have the same label as node i.

A subtree of a tree T is the tree consisting of a node in T and all of its descendant nodes.

Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], labels = "abaedcd"
Output: [2,1,1,1,1,1,1]
Explanation: Node 0 has label 'a' and its sub-tree has node 2 with label 'a' as well, thus the answer is 2. Notice that any node is part of its sub-tree.
Node 1 has a label 'b'. The sub-tree of node 1 contains nodes 1,4 and 5, as nodes 4 and 5 have different labels than node 1, the answer is just 1 (the node itself).

Input: n = 6, edges = [[0,1],[0,2],[1,3],[3,4],[4,5]], labels = "cbabaa"
Output: [1,2,1,1,2,1]

Input: n = 7, edges = [[0,1],[1,2],[2,3],[3,4],[4,5],[5,6]], labels = "aaabaaa"
Output: [6,5,4,1,3,2,1]

Constraints:
1 <= n <= 10^5
edges.length == n - 1
edges[i].length == 2
0 <= ai, bi < n
ai != bi
labels.length == n
labels is consisting of only of lower-case English letters.
'''
from collections import defaultdict 
class Solution:
    def dfs(self, node):
        self.traversed.add(node)
        color_dict = dict()
        c = self.labels[node]
        if node not in self.adj_table:
            return {c: 1}
        for n in self.adj_table[node]:
            if n in self.traversed:
                continue
            cd = self.dfs(n)
            color_dict = {k: cd.get(k, 0) + color_dict.get(k, 0) for k in set(cd) | set(color_dict)}
        color_dict[c] = color_dict.get(c, 0) + 1
        self.color_count[node] = color_dict[c]
        # print(c, color_dict)
        return color_dict

    def countSubTrees(self, n: int, edges, labels: str):
        self.labels = labels
        self.adj_table = defaultdict(list)
        for e in edges:
            self.adj_table[e[0]].append(e[1])
            self.adj_table[e[1]].append(e[0])

        self.color_count = [1 for _ in range(n)]
        self.traversed = set()
        self.dfs(0)
        return self.color_count

s = Solution()
n = 7
edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
labels = "abaedcd"
n = 7
edges = [[0,1],[1,2],[2,3],[3,4],[4,5],[5,6]]
labels = "aaabaaa"
# n = 6
# edges = [[0,1],[0,2],[1,3],[3,4],[4,5]]
# labels = "cbabaa"
# n = 7
# edges = [[0,1],[0,2],[2,3],[1,4],[4,5],[4,6]]
# labels = "feebadc"
# n = 4
# edges = [[0,2],[0,3],[1,2]]
# labels = "aeed"
print(s.countSubTrees(n, edges, labels))
