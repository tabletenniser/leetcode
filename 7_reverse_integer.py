"""
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

click to show spoilers.

Note:
    The input is assumed to be a 32-bit signed integer. Your function should return 0 when the reversed integer overflows.
"""
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = 0
        y = x if x >=0 else -x
        while y > 0:
            result += y % 10
            y /= 10
            if y == 0:
                break
            result *= 10
        if x < 0:
            result = -result

        if result >= 2**31 or result < -2**31:
            result = 0
        return result
