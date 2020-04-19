'''
You have a grid of size n x 3 and you want to paint each cell of the grid with exactly one of the three colours: Red, Yellow or Green while making sure that no two adjacent cells have the same colour (i.e no two cells that share vertical or horizontal sides have the same colour).

You are given n the number of rows of the grid.

Return the number of ways you can paint this grid. As the answer may grow large, the answer must be computed modulo 10^9 + 7.



Example 1:

Input: n = 1
Output: 12
Explanation: There are 12 possible way to paint the grid as shown:

Example 2:

Input: n = 2
Output: 54
Example 3:

Input: n = 3
Output: 246
Example 4:

Input: n = 7
Output: 106494
Example 5:

Input: n = 5000
Output: 30228214


Constraints:

n == grid.length
grid[i].length == 3
1 <= n <= 5000
'''
class Solution:
    def rec(self, n):
        if n in self.ht:
            return self.ht[n]
        if n == 1:
            # Number of 'ABC's and number of 'ABA's
            return 1, 1
        abc_s, aba_s = self.rec(n - 1)
        new_abc_s = 2 * abc_s + 2 * aba_s
        new_aba_s = 2 * abc_s + 3 * aba_s
        self.ht[n] = new_abc_s, new_aba_s
        return new_abc_s, new_aba_s

    def numOfWays(self, n: int) -> int:
        # self.ht = dict()
        # abc_s, aba_s = self.rec(n)
        abc_s, aba_s = 1, 1
        for _ in range(n - 1):
            new_abc_s = 2 * abc_s + 2 * aba_s
            new_aba_s = 2 * abc_s + 3 * aba_s
            aba_s, abc_s = new_aba_s, new_abc_s
        return ((abc_s + aba_s) * 6) % 1000000007


s = Solution()
n = 1
res = s.numOfWays(n)
print(res)

