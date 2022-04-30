'''
Given a 2D integer array circles where circles[i] = [xi, yi, ri] represents the center (xi, yi) and radius ri of the ith circle drawn on a grid, return the number of lattice points that are present inside at least one circle.
Note:
A lattice point is a point with integer coordinates.
Points that lie on the circumference of a circle are also considered to be inside it.

Example 1:
Input: circles = [[2,2,1]]
Output: 5
Explanation:
The figure above shows the given circle.
The lattice points present inside the circle are (1, 2), (2, 1), (2, 2), (2, 3), and (3, 2) and are shown in green.
Other points such as (1, 1) and (1, 3), which are shown in red, are not considered inside the circle.
Hence, the number of lattice points present inside at least one circle is 5.

Example 2:
Input: circles = [[2,2,2],[3,4,1]]
Output: 16
Explanation:
The figure above shows the given circles.
There are exactly 16 lattice points which are present inside at least one circle. 
Some of them are (0, 2), (2, 0), (2, 4), (3, 2), and (4, 4).

Constraints:
1 <= circles.length <= 200
circles[i].length == 3
1 <= xi, yi <= 100
1 <= ri <= min(xi, yi)
'''
class Solution:
    def countLatticePoints(self, circles) -> int:
        res = set()
        for (c_x, c_y, c_r) in circles:
            for x in range(c_x - c_r, c_x + c_r + 1):
                for y in range(c_y - c_r, c_y + c_r + 1):
                    if (c_x-x)**2+(c_y-y)**2 <= c_r**2:
                        res.add((x, y))
        return len(res)
        # res = set()
        # circles.sort(key = lambda x:x[-1], reverse=True)
        # res = 0
        # for x in range(201):
        #     for y in range(201):
        #         for (c_x, c_y, c_r) in circles:
        #             if (c_x-x)**2+(c_y-y)**2 <= c_r**2:
        #                 # print(x,y,c_x,c_y,c_r)
        #                 # res.add((x,y))
        #                 res += 1
        #                 break
        return res

s = Solution()
circles = [[2,9,2],[6,4,3],[6,1,1],[7,8,2],[5,3,1],[3,1,1],[3,7,3],[9,9,8],[7,4,3],[6,10,3],[9,8,6],[3,2,2],[2,8,2],[10,6,3],[2,3,2],[9,8,4],[3,5,3]] * 10
res = s.countLatticePoints(circles)
print(res)

