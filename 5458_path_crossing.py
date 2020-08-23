'''
'''
class Solution(object):
    def isPathCrossing(self, path):
        """
        :type n: int
        :rtype: List[int]
        """
        x, y = 0, 0
        traveled_cells = set()
        traveled_cells.add((0, 0))
        for d in path:
            if d == 'N':
                y += 1
            elif d == 'S':
                y -= 1
            elif d == 'E':
                x += 1
            elif d == 'W':
                x -= 1
            if (x,y) in traveled_cells:
                return False
            traveled_cells.add((x, y))
        return True

s = Solution()
print(s.isPathCrossing('NES'))
