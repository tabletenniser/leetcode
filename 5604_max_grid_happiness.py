'''
'''
class Solution:
    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
        grid = [[None for _ in range(n)] for _ in range(m)]
        ht = dict()
        visited = set()
        def rec(i, j, cur_score, ic, ec):
            if i < 0 or j < 0 or i >= m or j >=n or (ic + ec == 0) or (i,j) in visited:
                return cur_score
            # if (i,j,ic,ec,cur_score) in ht:
            #     return cur_score + ht[(i,j,ic,ec,cur_score)]
            visited.add((i,j))
            i_n, e_n = 0, 0
            for dir_i, dir_j in [(0,1),(1,0),(0,-1),(-1,0)]:
                a, b = i + dir_i, j + dir_j
                if 0 <= a < m and 0 <= b < n and grid[a][b] == 'I':
                    i_n += 1
                if 0 <= a < m and 0 <= b < n and grid[a][b] == 'E':
                    e_n += 1
            # always try placing extrovert
            res = cur_score
            if ec > 0 and (40 + 40*e_n - 10 * i_n) > 0:
            # if ec > 0:
                grid[i][j] = 'E'
                new_s = cur_score + 40 + 40*e_n - 10 * i_n
                res = max(res, rec(i-1, j, new_s, ic, ec-1))
                res = max(res, rec(i+1, j, new_s, ic, ec-1))
                res = max(res, rec(i, j-1, new_s, ic, ec-1))
                res = max(res, rec(i, j+1, new_s, ic, ec-1))
                grid[i][j] = None
            if ic > 0 and (120 - 10*e_n - 60 * i_n) > 0:
            # if ic > 0:
                grid[i][j] = 'I'
                new_s = cur_score + 120 - 10*e_n - 60 * i_n
                res = max(res, rec(i-1, j, new_s, ic-1, ec))
                res = max(res, rec(i+1, j, new_s, ic-1, ec))
                res = max(res, rec(i, j-1, new_s, ic-1, ec))
                res = max(res, rec(i, j+1, new_s, ic-1, ec))
                grid[i][j] = None
            res = max(res, rec(i-1, j, cur_score, ic, ec))
            res = max(res, rec(i+1, j, cur_score, ic, ec))
            res = max(res, rec(i, j-1, cur_score, ic, ec))
            res = max(res, rec(i, j+1, cur_score, ic, ec))
            ht[(i,j,ic,ec,cur_score)] = res - cur_score
            visited.remove((i,j))
            return res
        return rec(m-1, n-1, 0, introvertsCount, extrovertsCount)

m = 5
n = 5
introvertsCount = 3
extrovertsCount = 6
s = Solution()
print(s.getMaxGridHappiness(m, n, introvertsCount, extrovertsCount))
