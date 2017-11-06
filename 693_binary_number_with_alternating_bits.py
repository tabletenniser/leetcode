'''
Given a positive integer, check whether it has alternating bits or not.

Example 1:
Input: 5
Output: True
Explanation:
The binary representation of 5 is: 101
Example 2:
Input: 7
Output: False
Explanation:
The binary representation of 7 is: 111
'''
class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        m = n ^ (n >> 1)
        return m & (m + 1) == 0


s = Solution()
assert(s.hasAlternatingBits(1))
assert(s.hasAlternatingBits(2))
assert(not s.hasAlternatingBits(3))
assert(not s.hasAlternatingBits(4))
assert(s.hasAlternatingBits(5))
assert(not s.hasAlternatingBits(6))
assert(not s.hasAlternatingBits(7))
assert(not s.hasAlternatingBits(8))
assert(not s.hasAlternatingBits(9))
assert(s.hasAlternatingBits(10))
