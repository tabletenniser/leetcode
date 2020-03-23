'''
Given a m x n grid. Each cell of the grid represents a street. The street of grid[i][j] can be:
1 which means a street connecting the left cell and the right cell.
2 which means a street connecting the upper cell and the lower cell.
3 which means a street connecting the left cell and the lower cell.
4 which means a street connecting the right cell and the lower cell.
5 which means a street connecting the left cell and the upper cell.
6 which means a street connecting the right cell and the upper cell.


Input: grid = [[2,4,3],[6,5,2]]
Output: true
Explanation: As shown you can start at cell (0, 0) and visit all the cells of the grid to reach (m - 1, n - 1).
Example 2:


Input: grid = [[1,2,1],[1,2,1]]
Output: false
Explanation: As shown you the street at cell (0, 0) is not connected with any street of any other cell and you will get stuck at cell (0, 0)
Example 3:

Input: grid = [[1,1,2]]
Output: false
Explanation: You will get stuck at cell (0, 1) and you cannot reach cell (0, 2).
Example 4:

Input: grid = [[1,1,1,1,1,1,3]]
Output: true
Example 5:

Input: grid = [[2],[2],[2],[2],[2],[2],[6]]
Output: true
'''
class Solution:
    def nextSpot(self, i, j, d, grid):
        if i < 0 or j < 0 or i >= self.num_row or j >= self.num_col or d not in self.MAP[grid[i][j]]:
            return None
        # print(i, j, d, self.MAP[grid[i][j]])
        gridStr = self.MAP[grid[i][j]]
        if d == 'S':
            if 'R' in gridStr:
                return i, j+1, 'L'
            elif 'D' in gridStr:
                return i+1, j, 'U'
            assert False
        gridStr = self.MAP[grid[i][j]]
        nextD = list(set(gridStr) - {d})[0]
        if nextD == 'U':
            return i - 1, j, self.REV[nextD]
        elif nextD == 'D':
            return i + 1, j, self.REV[nextD]
        elif nextD == 'L':
            return i, j - 1, self.REV[nextD]
        elif nextD == 'R':
            return i, j + 1, self.REV[nextD]

    def hasValidPathSub(self, i, j, d, grid):
        while i != self.num_row - 1 or j != self.num_col - 1:
            r = self.nextSpot(i, j, d, grid)
            if r == None:
                return False
            i, j, d = r
        return d in self.MAP[grid[i][j]]

    def hasValidPath(self, grid):
        self.MAP = {1: 'LR', 2: 'UD', 3: 'LD', 4: 'DR', 5: 'UL', 6: 'UR'}
        self.REV = {'L': 'R', 'R': 'L', 'U': 'D', 'D': 'U'}
        self.num_row = len(grid)
        self.num_col = len(grid[0])

        return self.hasValidPathSub(0, 0, self.MAP[grid[0][0]][0], grid) or \
        self.hasValidPathSub(0, 0, self.MAP[grid[0][0]][1], grid)


s = Solution()
# grid = [[2],[2],[2],[2],[2],[2],[6]]
grid=[[4,1],[6,1]]
# grid = [[1,1,1,1,1,1,3]]
res = s.hasValidPath(grid)
print(res)

