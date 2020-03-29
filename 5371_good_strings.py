'''
Given the strings s1 and s2 of size n, and the string evil. Return the number of good strings.

A good string has size n, it is alphabetically greater than or equal to s1, it is alphabetically smaller than or equal to s2, and it does not contain the string evil as a substring. Since the answer can be a huge number, return this modulo 10^9 + 7.

Example 1:

Input: n = 2, s1 = "aa", s2 = "da", evil = "b"
Output: 51
Explanation: There are 25 good strings starting with 'a': "aa","ac","ad",...,"az". Then there are 25 good strings starting with 'c': "ca","cc","cd",...,"cz" and finally there is one good string starting with 'd': "da".
Example 2:

Input: n = 8, s1 = "leetcode", s2 = "leetgoes", evil = "leet"
Output: 0
Explanation: All strings greater than or equal to s1 and smaller than or equal to s2 start with the prefix "leet", therefore, there is not any good string.
Example 3:

Input: n = 2, s1 = "gx", s2 = "gz", evil = "x"
Output: 2


Constraints:

s1.length == n
s2.length == n
1 <= n <= 500
1 <= evil.length <= 50
All strings consist of lowercase English letters.
'''
class Solution:
    # Get number of strings before, not including string
    def getNumStr(self, n, string, evil):
        res = 0
        for i in range(n):
            c = string[i]
            rank = ord(c) - ord('a')
            num_digits = n - 1 - i
            multiplier = 26 ** num_digits
            j = 1
            while num_digits - len(evil) ** j > 0:
                power = num_digits - len(evil) ** j
                multiplier += ((-1) ** j) * (26 ** power) * 
            res += rank * multiplier
        return res

    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        num_str_before_s1 = self.getNumStr(n, s1, evil)
        num_str_before_s2 = self.getNumStr(n, s2, evil) + 1   # +1 to include
        return num_str_before_s2 - num_str_before_s1


s = Solution()
n = 2
s1 = "gx"
s2 = "gz"
evil = "x"
res = s.findGoodStrings(n, s1, s2, evil)
print(res)

# string = 'bcd'
# print(s.getNumStr(len(string), string))
