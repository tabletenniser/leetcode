'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
'''
import heapq
class Solution:
    def minPathSum(self, grid) -> int:
        res_grid = [[9999999 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        res_grid[0][0] = grid[0][0]
        options = []
        heapq.heappush(options, (res_grid[0][0], 0, 0))
        while len(options) > 0:
            weight,row,col = heapq.heappop(options)
            if row == len(grid) -1 and col == len(grid[0]) -1:
                return weight
            if row + 1 < len(grid):
                new_weight = weight + grid[row+1][col]
                if new_weight < res_grid[row+1][col]:
                    res_grid[row+1][col] = new_weight
                    heapq.heappush(options, (res_grid[row+1][col], row+1, col))
            if col + 1 < len(grid[0]):
                new_weight = weight + grid[row][col+1]
                if new_weight < res_grid[row][col+1]:
                    res_grid[row][col+1] = new_weight
                    heapq.heappush(options, (res_grid[row][col+1], row, col+1))
        print(res_grid)
        assert False
        return None

s = Solution()
# grid = [[7,1,3,5,8,9,9,2,1,9,0,8,3,1,6,6,9,5],[9,5,9,4,0,4,8,8,9,5,7,3,6,6,6,9,1,6],[8,2,9,1,3,1,9,7,2,5,3,1,2,4,8,2,8,8],[6,7,9,8,4,8,3,0,4,0,9,6,6,0,0,5,1,4],[7,1,3,1,8,8,3,1,2,1,5,0,2,1,9,1,1,4],[9,5,4,3,5,6,1,3,6,4,9,7,0,8,0,3,9,9],[1,4,2,5,8,7,7,0,0,7,1,2,1,2,7,7,7,4],[3,9,7,9,5,8,9,5,6,9,8,8,0,1,4,2,8,2],[1,5,2,2,2,5,6,3,9,3,1,7,9,6,8,6,8,3],[5,7,8,3,8,8,3,9,9,8,1,9,2,5,4,7,7,7],[2,3,2,4,8,5,1,7,2,9,5,2,4,2,9,2,8,7],[0,1,6,1,1,0,0,6,5,4,3,4,3,7,9,6,1,9]]
grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
res = s.minPathSum(grid)
print(res)
