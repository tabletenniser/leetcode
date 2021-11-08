'''
There are n uniquely-sized sticks whose lengths are integers from 1 to n. You want to arrange the sticks such that exactly k sticks are visible from the left. A stick is visible from the left if there are no longer sticks to the left of it.

For example, if the sticks are arranged [1,3,2,5,4], then the sticks with lengths 1, 3, and 5 are visible from the left.
Given n and k, return the number of such arrangements. Since the answer may be large, return it modulo 109 + 7.



Example 1:

Input: n = 3, k = 2
Output: 3
Explanation: [1,3,2], [2,3,1], and [2,1,3] are the only arrangements such that exactly 2 sticks are visible.
The visible sticks are underlined.
Example 2:

Input: n = 5, k = 5
Output: 1
Explanation: [1,2,3,4,5] is the only arrangement such that all 5 sticks are visible.
The visible sticks are underlined.
Example 3:

Input: n = 20, k = 11
Output: 647427950
Explanation: There are 647427950 (mod 109 + 7) ways to rearrange the sticks such that exactly 11 sticks are visible.

Constraints:
1 <= n <= 1000
1 <= k <= n
'''
from math import perm
from math import factorial
from functools import lru_cache

class Solution:
    @lru_cache(maxsize = 5000)
    def rec(self, n, k):
        if n < k:
            return 0
        if k == 1:
            return factorial(n-1) % 1000000007
        if n == k:
            return 1
        res = 0
        for i in range(1,n+1):
            if n-i < k - 1:
                break
            # delta = (self.rec(n-i, k-1) * comb(n-1,i-1) * factorial(i-1)) % 1000000007
            delta = (self.rec(n-i, k-1) * (perm(n-1,i-1) % 1000000007)) % 1000000007
            res = (res + delta) % 1000000007
        print(n, k, res)
        return res % 1000000007

    def rearrangeSticks(self, n: int, k: int) -> int:
        return self.rec(n, k) % 1000000007

s = Solution()
res = s.rearrangeSticks(400,200)
print(res)
