'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.
'''
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        # Binary search to find the row where target contains
        l, r = 0, len(matrix) - 1
        while l <= r:
            mid = (l + r) / 2
            if matrix[mid][0] == target:
                return True
            elif target < matrix[mid][0]:
                r = mid - 1
            else:
                l = mid + 1
        row = min((l + r + 1) / 2, len(matrix) - 1)
        if target < matrix[row][0]:
            if row == 0:
                return False
            row -= 1
        assert(target > matrix[row][0])

        # Do binary search in matrix[row]
        l, r = 0, len(matrix[row]) - 1
        while l <= r:
            mid = (l + r) / 2
            if matrix[row][mid] == target:
                return True
            elif target < matrix[row][mid]:
                r = mid - 1
            else:
                l = mid + 1
        return False


s = Solution()
print s.searchMatrix([[1]], 1)
print s.searchMatrix([[1]], 0)
print s.searchMatrix([[1]], 2)
print s.searchMatrix([
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]], 0)
print s.searchMatrix([
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]], 1)
print s.searchMatrix([
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]], 50)
print s.searchMatrix([
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]], 7)
print s.searchMatrix([
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]], 51)
