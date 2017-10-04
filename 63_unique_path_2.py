'''
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.

Note: m and n will be at most 100.
'''

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if len(obstacleGrid) == 0 or len(obstacleGrid[0]) == 0:
            return 0
        table = [[0 for _ in xrange(len(obstacleGrid[0]))] for _ in xrange(len(obstacleGrid))]
        # Initial condition
        for i in xrange(0, len(obstacleGrid)):
            if obstacleGrid[i][0] == 1:
                break
            table[i][0] = 1
        for i in xrange(0, len(obstacleGrid[0])):
            if obstacleGrid[0][i] == 1:
                break
            table[0][i] = 1

        # Populate dp table
        for i in xrange(1, len(obstacleGrid)):
            for j in xrange(1, len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    continue
                table[i][j] = table[i-1][j] + table[i][j-1]
        return table[-1][-1]

s = Solution()
print s.uniquePathsWithObstacles(
[
  [1, 0],
])
print s.uniquePathsWithObstacles(
[
  [0],
])
print s.uniquePathsWithObstacles(
[
  [0, 1],
])
print s.uniquePathsWithObstacles(
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
])
print s.uniquePathsWithObstacles(
[
  [0,0,0],
  [1,0,1],
  [0,0,0]
])
