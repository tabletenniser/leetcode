'''

Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
'''
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0 for _ in xrange(n)] for _ in xrange(n)]
        i = 0
        num = 1
        while i <= n / 2:
            for j in xrange(i, n - i):
                res[i][j] = num
                num += 1
            for j in xrange(i + 1, n - i - 1):
                res[j][n - i - 1] = num
                num += 1
            if i == n / 2 and n % 2 ==1:
                break
            for j in xrange(n - i - 1, i - 1, -1):
                res[n - i - 1][j] = num
                num += 1
            for j in xrange(n - i - 2, i, -1):
                res[j][i] = num
                num += 1
            i += 1
            print "res", res
        return res

s = Solution()
m = s.generateMatrix(3)
for row in m:
    print row
m = s.generateMatrix(4)
for row in m:
    print row
