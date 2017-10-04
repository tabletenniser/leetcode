'''
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.
'''
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = [i+1 for i in xrange(n)]
        res = ''
        import math
        while n > 0:
            assert(k > 0)
            fact = math.factorial(n-1)
            ind = (k-1) / fact
            res += str(nums[ind])
            del nums[ind]
            k -= ind * fact
            n -= 1
        return res

s = Solution()
print s.getPermutation(3, 3)
print s.getPermutation(4, 24)
