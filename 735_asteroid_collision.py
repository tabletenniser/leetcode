'''
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left).

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode.

Example 1:
Input: 
asteroids = [5, 10, -5]
Output: [5, 10]
Explanation: 
The 10 and -5 collide resulting in 10.  The 5 and 10 never collide.
Example 2:
Input: 
asteroids = [8, -8]
Output: []
Explanation: 
The 8 and -8 collide exploding each other.
Example 3:
Input: 
asteroids = [10, 2, -5]
Output: [10]
Explanation: 
The 2 and -5 collide resulting in -5.  The 10 and -5 collide resulting in 10.
Note:

The length of asteroids will be at most 10000.
Each asteroid will be a non-zero integer in the range [-1000, 1000]..
'''
class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        def has_different_sign(num1, num2):
            assert(num1 != 0 and num2 != 0)
            if num1 > 0 and num2 > 0 or num1 < 0 and num2 < 0:
                return False
            return True
        result = []
        i = 0
        last_direction = None
        while i < len(asteroids):
            a = asteroids[i]
            if last_direction == None:
                result.append(a)
            elif last_direction == 1 and a > 0 or last_direction == -1:
                result.append(a)
            else:
                new_asteroid_destroyed = False
                while len(result) > 0 and has_different_sign(result[-1], a):
                    last_asteroid = result[-1]
                    if abs(a) >= abs(last_asteroid):
                        del result[-1]
                    if abs(a) <= abs(last_asteroid):
                        new_asteroid_destroyed = True
                        break
                if not new_asteroid_destroyed:
                    result.append(a)
            last_direction = result[-1]/abs(result[-1]) if len(result) > 0 else None
            i += 1
        return result

s = Solution()
assert s.asteroidCollision([9, -9]) == []
assert s.asteroidCollision([10, 2, -5]) == [10]
assert s.asteroidCollision([5, 10, -5]) == [5, 10]
assert s.asteroidCollision([1, -1, 1, -1]) == []
assert s.asteroidCollision([1, -1, 2, -1, -1]) == [2]
assert s.asteroidCollision([1, -3, 2, -1, -1]) == [-3, 2]
assert s.asteroidCollision([1, -3, 2, -5, -1]) == [-3, -5, -1]
assert s.asteroidCollision([8, -3, 2, -5, -1]) == [8]
