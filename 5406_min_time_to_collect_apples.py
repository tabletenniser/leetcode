'''
Given an undirected tree consisting of n vertices numbered from 0 to n-1, which has some apples in their vertices. You spend 1 second to walk over one edge of the tree. Return the minimum time in seconds you have to spend in order to collect all apples in the tree starting at vertex 0 and coming back to this vertex.
The edges of the undirected tree are given in the array edges, where edges[i] = [fromi, toi] means that exists an edge connecting the vertices fromi and toi. Additionally, there is a boolean array hasApple, where hasApple[i] = true means that vertex i has an apple, otherwise, it does not have any apple.

Example 1:
Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,true,false,true,true,false]
Output: 8
Explanation: The figure above represents the given tree where red vertices have an apple. One optimal path to collect all apples is shown by the green arrows.

Example 2:
Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,true,false,false,true,false]
Output: 6
Explanation: The figure above represents the given tree where red vertices have an apple. One optimal path to collect all apples is shown by the green arrows.

Example 3:
Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,false,false,false,false,false]
Output: 0

Constraints:
1 <= n <= 10^5
edges.length == n-1
edges[i].length == 2
0 <= fromi, toi <= n-1
fromi < toi
hasApple.length == n
'''
from collections import defaultdict
# import heapq
class Solution:
    def dfs(self, n, tree_map, apple_set, travered):
        travered.add(n)
        next_step = []
        for n_node in tree_map[n]:
            if n_node not in travered:
                next_step.append(n_node)
        if len(next_step) == 0: # leaf node
            return 1 if n in apple_set else 0
        child_node_sum = 0
        for n_node in next_step:
            child_node_sum += self.dfs(n_node, tree_map, apple_set, travered)
        #print(n, child_node_sum+1)
        if n == 0: return child_node_sum
        return 0 if (child_node_sum == 0 and n not in apple_set) else child_node_sum + 1

    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        self.res = 0
        num_of_edges = 2 * n - 2
        res = num_of_edges
        tree_map = defaultdict(list)
        for e in edges:
            tree_map[e[0]].append(e[1])
            tree_map[e[1]].append(e[0])
        apple_set = set([0])    # 0 must be there
        for index,boolean in enumerate(hasApple):
            if boolean:
                apple_set.add(index)
        travered = set([0])
        return self.dfs(0, tree_map, apple_set, travered) * 2
        #
        # q = []
        # for node in len(n):
        #     q.append((len(tree_map[node]), node))
        # heapq.heapify(q)
        # print(q)
        # while len(q) > 0:
        #     outgoing_n_count, node = heapq.heappop(q)
        #     if outgoing_n_count > 1:
        #         break
        #     if node not in apple_set:
        #         res -= 2
        #         connected_n = tree_map[node]
        #         tree_map[connected_n].remove(node)
        # return res





s = Solution()
nums = [0,1,2,3,4]
index = [0,1,2,2,1]
res = s.createTargetArray(nums, index)
print(res)

