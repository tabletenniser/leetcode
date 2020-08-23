'''
A delivery company wants to build a new service centre in a new city. The company knows the positions of all the customers in this city on a 2D-Map and wants to build the new centre in a position such that the sum of the euclidean distances to all customers is minimum.
Given an array positions where positions[i] = [xi, yi] is the position of the ith customer on the map, return the minimum sum of the euclidean distances to all customers.
In other words, you need to choose the position of the service centre [xcentre, ycentre] such that the following formula is minimized:
Answers within 10^-5 of the actual value will be accepted.

Example 1:
Input: positions = [[0,1],[1,0],[1,2],[2,1]]
Output: 4.00000
Explanation: As shown, you can see that choosing [xcentre, ycentre] = [1, 1] will make the distance to each customer = 1, the sum of all distances is 4 which is the minimum possible we can achieve.

Example 2:
Input: positions = [[1,1],[3,3]]
Output: 2.82843
Explanation: The minimum possible sum of distances = sqrt(2) + sqrt(2) = 2.82843

Example 3:
Input: positions = [[1,1]]
Output: 0.00000

Example 4:
Input: positions = [[1,1],[0,0],[2,0]]
Output: 2.73205
Explanation: At the first glance, you may think that locating the centre at [1, 0] will achieve the minimum sum, but locating it at [1, 0] will make the sum of distances = 3.
Try to locate the centre at [1.0, 0.5773502711] you will see that the sum of distances is 2.73205.
Be careful with the precision!

Example 5:
Input: positions = [[0,1],[3,2],[4,5],[7,6],[8,9],[11,1],[2,12]]
Output: 32.94036
Explanation: You can use [4.3460852395, 4.9813795505] as the position of the centre.

Constraints:
1 <= positions.length <= 50
positions[i].length == 2
0 <= positions[i][0], positions[i][1] <= 100
'''
import math
class Solution:
    def getMinDistSum(self, positions) -> float:
        if len(positions) <= 1:
            return 0
        step_tolerance = 0.00000000001
        cst = 40
        step_size = cst
        xs = [p[0] for p in positions]
        ys = [p[1] for p in positions]
        x = sum(xs) / len(xs) + 0.01
        y = sum(ys) / len(ys) - 0.01
        def distance(x,a,y,b):
            return math.sqrt((x-a)**2 + (y-b)**2)

        i = 0
        p_total_d = -100000
        while True:
            dx = 0
            dy = 0
            total_d = 0
            for (a,b) in positions:
                d = distance(x,a,y,b)
                # if d != 0:
                dx += (x-a) / d
                dy += (y-b) / d
                total_d += d
            # print(x,y,dx,dy,total_d,step_size)
            delta_x = step_size * dx
            delta_y = step_size * dy
            # if abs(total_d - p_total_d) < step_tolerance:
            if step_size < 1e-11:
                return total_d
            p_total_d = total_d
            x -= delta_x
            y -= delta_y
            if i == 80:
                i = 0
                step_size = step_size / 2
            i += 1


sol = Solution()
positions = [[0,1],[3,2],[4,5],[7,6],[8,9],[11,1],[2,12]]
# positions = [[1,1],[0,0],[2,0]]
# positions = [[0,1],[1,0],[1,2],[2,1]]
# positions = [[0,1],[1,0],[1,2],[2,1],[1,1]]
# positions = [[58,32],[41,21]]
# positions = [[1,1]]
positions = [[1,1],[3,3]]
positions = [[9,9],[31,1],[28,61],[14,42],[95,98],[37,69]]
positions = [[96,97],[46,17],[95,97],[96,95],[97,95],[55,56],[98,96],[50,44],[37,72],[38,21],[96,96],[96,97],[47,62],[97,97],[46,51],[98,97],[42,25],[65,62],[18,71],[94,95],[48,44],[96,95],[97,97],[33,54],[22,37],[95,96],[34,47],[94,98],[95,97],[43,20]]
print(sol.getMinDistSum(positions))
