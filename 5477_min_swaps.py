'''
Given an n x n binary grid, in one step you can choose two adjacent rows of the grid and swap them.
A grid is said to be valid if all the cells above the main diagonal are zeros.
Return the minimum number of steps needed to make the grid valid, or -1 if the grid cannot be valid.
The main diagonal of a grid is the diagonal that starts at cell (1, 1) and ends at cell (n, n).

Input: grid = [[0,0,1],[1,1,0],[1,0,0]]
Output: 3
Input: grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
Output: -1
Input: grid = [[1,0,0],[1,1,0],[1,1,1]]
Output: 0

Constraints:
n == grid.length
n == grid[i].length
1 <= n <= 200
'''
class Solution:
    def get_right_most_one(self, row):
        for i in range(len(row)-1, -1, -1):
            if row[i] == 1:
                return i
        return -1

    def rec(self, grid, cur_r):
        if cur_r == len(grid):
            return 0
        target_row = None
        for i, rmo in enumerate(self.rmo[cur_r:]):
            if rmo <= cur_r:
                target_row = i + cur_r
                break
        if target_row == None:
            return -1
        print(grid,self.rmo,cur_r,target_row)
        res = 0
        for i in range(target_row-1, cur_r-1, -1):
            grid[i],grid[i+1] = grid[i+1],grid[i]
            self.rmo[i],self.rmo[i+1] = self.rmo[i+1],self.rmo[i]
            res += 1
        sub = self.rec(grid, cur_r + 1)
        if sub == -1:
            return -1
        return res + sub

    def minSwaps(self, grid) -> int:
        self.rmo = []
        for row in grid:
            self.rmo.append(self.get_right_most_one(row))
        return self.rec(grid, 0)


grid = [[0,0,1],[1,1,0],[1,0,0]]
grid = [[1,0,1],[1,1,0],[1,1,1]]
grid = [[1,0,0,0,0,0],[0,0,0,1,0,0],[0,0,0,1,0,0],[0,0,1,0,0,0],[0,1,0,0,0,0],[0,0,0,0,0,1]]
s = Solution()
print(s.minSwaps(grid))
