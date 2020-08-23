'''
Given a binary string s (a string consisting only of '0' and '1's).
Return the number of substrings with all characters 1's.
Since the answer may be too large, return it modulo 10^9 + 7.

Example 1:
Input: s = "0110111"
Output: 9
Explanation: There are 9 substring in total with only 1's characters.
"1" -> 5 times.
"11" -> 3 times.
"111" -> 1 time.
Example 2:

Input: s = "101"
Output: 2
Explanation: Substring "1" is shown 2 times in s.
Example 3:

Input: s = "111111"
Output: 21
Explanation: Each substring contains only 1's characters.
Example 4:

Input: s = "000"
Output: 0

Constraints:
s[i] == '0' or s[i] == '1'
1 <= s.length <= 10^5
'''
class Solution:
    def numSub(self, s: str) -> int:
        c = 0
        i = 0
        res = 0
        while i < len(s):
            if s[i] == '1':
                c += 1
            else:
                res += c * (c+1) // 2
                c = 0
            i += 1
        res += c * (c+1) // 2
        return res

sol = Solution()
s = "111111"
s = "0110111"
print(sol.numSub(s))
