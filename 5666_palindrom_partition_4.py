'''
Given a string s, return true if it is possible to split the string s into three non-empty palindromic substrings. Otherwise, return false.
A string is said to be palindrome if it the same string when reversed.

Example 1:
Input: s = "abcbdd"
Output: true
Explanation: "abcbdd" = "a" + "bcb" + "dd", and all three substrings are palindromes.

Example 2:
Input: s = "bcbddxy"
Output: false
Explanation: s cannot be split into 3 palindromes.

Constraints:
3 <= s.length <= 2000
s consists only of lowercase English letters.
'''
from functools import lru_cache
class Solution:
    @lru_cache(maxsize = 10000)
    def rec(self, s, p):
        self.count+=1
        if p == 1:
            return s == s[::-1]
        # print(s,p)
        l = len(s)
        for i in range(l):
            subStr = s[:i]
            if subStr == subStr[::-1]:
                res = self.rec(s[i:], p-1)
                if res == True:
                    return res
        return False

    def checkPartitioning(self, s: str) -> bool:
        self.count = 0
        res = self.rec(s, 3)
        print(self.count)
        return res


sol = Solution()
s = "abcbdd"*300
s = "abcba"*2000
# s = "bcbddxy"
print(sol.checkPartitioning(s))
