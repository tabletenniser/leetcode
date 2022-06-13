'''
A parentheses string is a non-empty string consisting only of '(' and ')'. It is valid if any of the following conditions is true:

It is ().
It can be written as AB (A concatenated with B), where A and B are valid parentheses strings.
It can be written as (A), where A is a valid parentheses string.
You are given an m x n matrix of parentheses grid. A valid parentheses string path in the grid is a path satisfying all of the following conditions:

The path starts from the upper left cell (0, 0).
The path ends at the bottom-right cell (m - 1, n - 1).
The path only ever moves down or right.
The resulting parentheses string formed by the path is valid.
Return true if there exists a valid parentheses string path in the grid. Otherwise, return false.

Example 1:
Input: grid = [["(","(","("],[")","(",")"],["(","(",")"],["(","(",")"]]
Output: true
Explanation: The above diagram shows two possible paths that form valid parentheses strings.
The first path shown results in the valid parentheses string "()(())".
The second path shown results in the valid parentheses string "((()))".
Note that there may be other valid parentheses string paths.
Example 2:
Input: grid = [[")",")"],["(","("]]
Output: false
Explanation: The two possible paths form the parentheses strings "))(" and ")((". Since neither of them are valid parentheses strings, we return false.
Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 100
grid[i][j] is either '(' or ')'.
'''
class Solution:
    def hasValidPath(self, grid) -> bool:
        m = len(grid)
        n = len(grid[0])
        ht = {}
        def rec(i, j, left_count):
            if (i,j,left_count) in ht:
                return ht[(i,j,left_count)]
            if i == m - 1 and j == n - 1:
                return left_count == 1 and grid[i][j] == ')'
            if i >= m or j >= n or left_count < 0:
                return False
            if grid[i][j] == '(':
                res = rec(i+1, j, left_count + 1) or rec(i, j + 1, left_count + 1)
            else:
                res = rec(i+1, j, left_count - 1) or rec(i, j + 1, left_count - 1)
            # print(i,j,res)
            ht[(i,j,left_count)] = res
            return res
        return rec(0, 0, 0)

s = Solution()
grid = [["(","(","("],[")","(",")"],["(","(",")"],["(","(",")"]]
# grid = [[")",")"],["(","("]]
res = s.hasValidPath(grid)
print(res)
