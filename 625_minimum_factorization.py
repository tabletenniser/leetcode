"""

Given a positive integer a, find the smallest positive integer b whose multiplication of each digit equals to a.

If there is no answer or the answer is not fit in 32-bit signed integer, then return 0.

Example 1
Input:

48 
Output:
68
Example 2
Input:

15
Output:
35
Discuss

"""
class Solution(object):
    def smallestFactorization(self, a):
        """
        :type a: int
        :rtype: int
        """
        if a <= 1:
            return a
        factors = []
        while a > 1:
            foundDivisor = False
            for f in xrange(9,1,-1):
                if a % f == 0:
                    factors.append(str(f))
                    a /= f
                    foundDivisor = True
                    break
            if not foundDivisor:
                return 0
        factors = factors[::-1]
        result = int(''.join(factors))
        return result if result < 2**31 else 0
