'''
661. Image Smoother My SubmissionsBack to Contest
Given a 2D integer matrix M representing the gray scale of an image, you need to design a smoother to make the gray scale of each cell becomes the average gray scale (rounding down) of all the 8 surrounding cells and itself. If a cell has less than 8 surrounding cells, then use as many as you can.

Example 1:
Input:
[[1,1,1],
 [1,0,1],
 [1,1,1]]
Output:
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]
Explanation:
For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0
Note:
The value in the given matrix is in the range of [0, 255].
The length and width of the given matrix are in the range of [1, 150].
'''
class Solution(object):
    def add(self, M, i, j, s, c):
        if i>=0 and j>=0 and i<len(M) and j<len(M[0]):
            s += M[i][j]
            c += 1
        return s,c

    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(M) == 0:
            return []
        w = len(M)
        l = len(M[0])
        r = [[0 for _ in xrange(l)] for _ in xrange(w)]
        for i in xrange(w):
            for j in xrange(l):
                s,c = M[i][j], 1
                s,c = self.add(M, i-1, j, s, c)
                s,c = self.add(M, i, j-1, s, c)
                s,c = self.add(M, i+1, j, s, c)
                s,c = self.add(M, i, j+1, s, c)
                s,c = self.add(M, i-1, j-1, s, c)
                s,c = self.add(M, i-1, j+1, s, c)
                s,c = self.add(M, i+1, j-1, s, c)
                s,c = self.add(M, i+1, j+1, s, c)
                r[i][j] = s/c
        return r
