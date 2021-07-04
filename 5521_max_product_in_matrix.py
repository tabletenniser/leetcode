'''
'''
class Solution:
    def maxProductPath(self, grid) -> int:
        m, n = len(grid) - 1, len(grid[0]) - 1
        ht = dict()
        def rec(r, c):
            if (r,c) in ht:
                return ht[(r,c)]
            if r > m or c > n:
                return -1, 1, False
            max_p = grid[r][c] if grid[r][c] > 0 else -1
            max_n = grid[r][c] if grid[r][c] < 0 else 1
            if r == m and c == n:
                if grid[r][c] == 0:
                    return 0,0
                return max_p, max_n
            down_res = rec(r+1, c)
            right_res = rec(r, c+1)
            if grid[r][c] > 0:
                res = grid[r][c] * max(down_res[0], right_res[0]), grid[r][c] * min(down_res[1], right_res[1])
            elif grid[r][c] < 0:
                res = grid[r][c] * min(down_res[1], right_res[1]), grid[r][c] * max(down_res[0], right_res[0])
            else:
                res = 0, 0
            # print(r,c,res)
            ht[(r,c)] = res
            return res
        result = max(-1, rec(0, 0)[0])
        return result % 1000000007 if result > 0 else result

grid = [[-1,1,-2,-1],[3,-3,-2,0]]
grid = [[3]*15]*15
grid = [[-1,-2,-3],[-2,-3,-3],[-3,-3,-2]]
sol = Solution()
print(sol.maxProductPath(grid))
