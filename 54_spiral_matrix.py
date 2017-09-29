'''

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].

'''

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        i, j = 0, 0
        i_min, j_min = 0, 0
        i_max, j_max = len(matrix) - 1, len(matrix[0]) - 1
        while i_min <= i_max and j_min <= j_max:
            i = i_min
            while i < i_max:
                result.append(matrix[i][j_min])
                i += 1
            j = j_min
            while j < j_max:
                result.append(matrix[i_max][j])
                j += 1
            i = i_max
            while i > i_min and j_max > j_min:
                result.append(matrix[i][j_max])
                i -= 1
            j = j_max
            while j > j_min and i_max > i_min:
                result.append(matrix[i_min][j])
                j -= 1
            i_min += 1
            j_min += 1
            i_max -= 1
            j_max -= 1
        return result
