'''
There are n cars traveling at different speeds in the same direction along a one-lane road. You are given an array cars of length n, where cars[i] = [positioni, speedi] represents:

positioni is the distance between the ith car and the beginning of the road in meters. It is guaranteed that positioni < positioni+1.
speedi is the initial speed of the ith car in meters per second.
For simplicity, cars can be considered as points moving along the number line. Two cars collide when they occupy the same position. Once a car collides with another car, they unite and form a single car fleet. The cars in the formed fleet will have the same position and the same speed, which is the initial speed of the slowest car in the fleet.

Return an array answer, where answer[i] is the time, in seconds, at which the ith car collides with the next car, or -1 if the car does not collide with the next car. Answers within 10-5 of the actual answers are accepted.

Example 1:
Input: cars = [[1,2],[2,1],[4,3],[7,2]]
Output: [1.00000,-1.00000,3.00000,-1.00000]
Explanation: After exactly one second, the first car will collide with the second car, and form a car fleet with speed 1 m/s. After exactly 3 seconds, the third car will collide with the fourth car, and form a car fleet with speed 2 m/s.

Example 2:
Input: cars = [[3,4],[5,4],[6,3],[9,1]]
Output: [2.00000,1.00000,1.50000,-1.00000]

Constraints:
1 <= cars.length <= 105
1 <= positioni, speedi <= 106
positioni < positioni+1
'''
MAX_INT = 9999999999
class Solution:
    def getCollisionTimes(self, cars):
        l = len(cars)
        res = [-1.0 for _ in range(l)]
        upper = l-1
        for i in range(l-1, -1, -1):
            val = MAX_INT
            p_i, s_i = cars[i]
            for j in range(i, upper+1, 1):
                # print(i,j,res)
                p_j, s_j = cars[j]
                if s_i > s_j:
                    cur_val = (p_j - p_i) / (s_i - s_j)
                    if cur_val < val:
                        val = cur_val
            if val == MAX_INT:
                res[i] = -1.0
                upper = i
            else:
                res[i] = val
        return res


s = Solution()
cars = [[3,4],[5,4],[6,3],[9,1]]
cars = [[1,2],[2,1],[4,3],[7,2]]
cars = [[i, i] for i in range(1000000)]
cars = [[i, 10000-i] for i in range(10000)]
print(s.getCollisionTimes(cars))
