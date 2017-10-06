'''
On an NxN chessboard, a knight starts at the r-th row and c-th column and attempts to make exactly K moves. The rows and columns are 0 indexed, so the top-left square is (0, 0), and the bottom-right square is (N-1, N-1).

A chess knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.


Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece would go off the chessboard) and moves there.

The knight continues moving until it has made exactly K moves or has moved off the chessboard. Return the probability that the knight remains on the board after it has stopped moving.

Example:
Input: 3, 2, 0, 0
Output: 0.0625
Explanation: There are two moves (to (1,2), (2,1)) that will keep the knight on the board.
From each of those positions, there are also two moves that will keep the knight on the board.
The total probability the knight stays on the board is 0.0625.
Note:
N will be between 1 and 25.
K will be between 0 and 100.
The knight always initially starts on the board.
'''
class Solution(object):
    def kp_rec(self, N, K, r, c, kp):
        if r < 0 or c < 0 or r >= N or c >= N:
            return 0.0
        if K == 0:
            return 1.0
        if (K, r, c) in kp:
            return kp[(K, r, c)]
        total_prob = 0
        for d in [(1,2), (2,1), (-1, -2), (-2, -1), (1, -2), (-1, 2), (2, -1), (-2, 1)]:
            total_prob += self.kp_rec(N, K-1, r+d[0], c+d[1], kp) * 1.0/8

        kp[(K, r, c)] = total_prob
        return total_prob

    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        kp = dict()
        res = self.kp_rec(N, K, r, c, kp)
        return res

s = Solution()
# print s.knightProbability(3, 2, 0, 0)
print s.knightProbability(8, 30, 6, 4)
