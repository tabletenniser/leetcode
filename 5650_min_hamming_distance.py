'''
You are given two integer arrays, source and target, both of length n. You are also given an array allowedSwaps where each allowedSwaps[i] = [ai, bi] indicates that you are allowed to swap the elements at index ai and index bi (0-indexed) of array source. Note that you can swap elements at a specific pair of indices multiple times and in any order.

The Hamming distance of two arrays of the same length, source and target, is the number of positions where the elements are different. Formally, it is the number of indices i for 0 <= i <= n-1 where source[i] != target[i] (0-indexed).

Return the minimum Hamming distance of source and target after performing any amount of swap operations on array source.



Example 1:

Input: source = [1,2,3,4], target = [2,1,4,5], allowedSwaps = [[0,1],[2,3]]
Output: 1
Explanation: source can be transformed the following way:
- Swap indices 0 and 1: source = [2,1,3,4]
- Swap indices 2 and 3: source = [2,1,4,3]
The Hamming distance of source and target is 1 as they differ in 1 position: index 3.
Example 2:

Input: source = [1,2,3,4], target = [1,3,2,4], allowedSwaps = []
Output: 2
Explanation: There are no allowed swaps.
The Hamming distance of source and target is 2 as they differ in 2 positions: index 1 and index 2.
Example 3:

Input: source = [5,1,2,4,3], target = [1,5,4,2,3], allowedSwaps = [[0,4],[4,2],[1,3],[1,4]]
Output: 0


Constraints:

n == source.length == target.length
1 <= n <= 105
1 <= source[i], target[i] <= 105
0 <= allowedSwaps.length <= 105
allowedSwaps[i].length == 2
0 <= ai, bi <= n - 1
ai != bi
'''
class Solution:
    def find(self, parent, i):
        if (parent[i] == -1):
            return i, 0
        root, rank = self.find(parent, parent[i])
        return root, rank+1

    def union(self, parent, x, y):
        xset, x_rank = self.find(parent, x)
        yset, y_rank = self.find(parent, y)
        if x_rank < y_rank:
            parent[xset] = yset
        else:
            parent[yset] = xset
        return

    def minimumHammingDistance(self, source, target, allowedSwaps) -> int:
        n = len(source)
        lt = {}
        for i, num in enumerate(source):
            lt[num] = lt.get(num, []) + [i]
        # print(lt)

        parent = {}
        for i in range(n):
            parent[i] = -1
        for a,b in allowedSwaps:
            if self.find(parent, a)[0] == self.find(parent, b)[0]:
                continue
            self.union(parent, a, b)
        # print(parent)

        i = 0
        res = 0
        while i < n:
            if source[i] == target[i]:
                i += 1
                continue
            # print(i, target[i], lt[target[i]])
            switched = False
            if target[i] in lt:
                for j in lt[target[i]]:
                    # print(i, j, self.find(parent,i), self.find(parent, j))
                    if self.find(parent, i)[0] == self.find(parent, j)[0]:
                        source[i], source[j] = source[j], source[i]
                        switched = True
                        break
            if not switched:
                res += 1
            # print(i, source)
            i += 1
        return res

s = Solution()
source = [5,1,2,4,3]
target = [1,5,4,2,3]
allowedSwaps = [[0,4],[4,2],[1,3],[1,4],[0,3]]
source=[18,67,10,36,17,62,38,78,52]
target=[3,4,99,36,26,58,29,33,74]
allowedSwaps=[[4,7],[3,1],[8,4],[5,6],[2,8],[0,7],[1,6],[3,7],[2,5],[3,0],[8,5],[2,1],[6,7],[5,1],[3,6],[4,0],[7,2],[2,6],[4,1],[3,2],[8,6],[8,0],[5,3],[1,0],[4,6],[8,7],[5,7],[3,8],[6,0],[8,1],[7,1],[5,0],[4,3],[0,2]]
print(s.minimumHammingDistance(source, target, allowedSwaps))
