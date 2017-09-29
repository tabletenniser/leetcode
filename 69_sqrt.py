'''
Implement int sqrt(int x).

Compute and return the square root of x.
'''
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l, r = 0, x
        while l < r:
            mid = (l + r) / 2
            square = mid*mid
            if square == x:
                return mid
            elif square < x:
                l = mid + 1
            else:
                r = mid
        return l if l*l <= x else l-1

s = Solution()
print s.mySqrt(0)
print s.mySqrt(1)
print s.mySqrt(2)
print s.mySqrt(3)
print s.mySqrt(4)
print s.mySqrt(5)
print s.mySqrt(81)
print s.mySqrt(80)
print s.mySqrt(82)
