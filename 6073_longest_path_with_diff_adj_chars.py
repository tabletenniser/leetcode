'''
You are given a tree (i.e. a connected, undirected graph that has no cycles) rooted at node 0 consisting of n nodes numbered from 0 to n - 1. The tree is represented by a 0-indexed array parent of size n, where parent[i] is the parent of node i. Since node 0 is the root, parent[0] == -1.

You are also given a string s of length n, where s[i] is the character assigned to node i.

Return the length of the longest path in the tree such that no pair of adjacent nodes on the path have the same character assigned to them.

Example 1:
Input: parent = [-1,0,0,1,1,2], s = "abacbe"
Output: 3
Explanation: The longest path where each two adjacent nodes have different characters in the tree is the path: 0 -> 1 -> 3. The length of this path is 3, so 3 is returned.
It can be proven that there is no longer path that satisfies the conditions. 

Example 2:
Input: parent = [-1,0,0,0], s = "aabc"
Output: 3
Explanation: The longest path where each two adjacent nodes have different characters is the path: 2 -> 0 -> 3. The length of this path is 3, so 3 is returned.
Constraints:
n == parent.length == s.length
1 <= n <= 105
0 <= parent[i] <= n - 1 for all i >= 1
parent[0] == -1
parent represents a valid tree.
s consists of only lowercase English letters.
'''
class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        adj_matrix = defaultdict(list)
        for a, b in enumerate(parent[1:]):
            adj_matrix[a+1].append(b)
            adj_matrix[b].append(a+1)
        # print(adj_matrix)
        traversed = set()
        # returns tuple: [longest, single_length]
        res = 0
        def dfs(node):
            nonlocal res
            traversed.add(node)
            next_elems = adj_matrix[node]
            longest_path_so_far = 1
            heap = []
            for elem in next_elems:
                if elem in traversed:
                    continue
                longest, path_l = dfs(elem)
                longest_path_so_far = max(longest, longest_path_so_far)
                if s[elem] != s[node]:
                    heapq.heappush(heap, path_l)
                if len(heap) > 2:
                    heapq.heappop(heap)
            if len(heap) > 0:
                longest_path_so_far = sum(heap) + 1
            longest_subpath = max(heap)+1 if len(heap) > 0 else 1
            # print(node, s[node], longest_path_so_far, longest_subpath)
            res = max(res, longest_path_so_far)
            return longest_path_so_far, longest_subpath
        dfs(0)
        return res
