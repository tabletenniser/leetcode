'''
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

click to show follow up.

Follow up:
Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
'''
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return

        # Booleans on whether first row / column needs to be zeroed
        zero_first_row = 0 in matrix[0]
        zero_first_col = 0 in [matrix[i][0] for i in xrange(len(matrix))]

        # Fill in first row / column info
        for i in xrange(1, len(matrix)):
            for j in xrange(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        # Zero based on values in first column
        for i in xrange(1, len(matrix)):
            if matrix[i][0] == 0:
                for j in xrange(1, len(matrix[0])):
                    matrix[i][j] = 0
        # Zero based on values in first row
        for i in xrange(1, len(matrix[0])):
            if matrix[0][i] == 0:
                for j in xrange(1, len(matrix)):
                    matrix[j][i] = 0

        if zero_first_row:
            for j in xrange(len(matrix[0])):
                matrix[0][j] = 0
        if zero_first_col:
            for j in xrange(len(matrix)):
                matrix[j][0] = 0

        return

s = Solution()
m = [[1,2,3], [4,5,6], [7,8,0]]
s.setZeroes(m)
for row in m:
    print row
