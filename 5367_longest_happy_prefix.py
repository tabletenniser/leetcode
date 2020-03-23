'''
A string is called a happy prefix if is a non-empty prefix which is also a suffix (excluding itself).

Given a string s. Return the longest happy prefix of s .

Return an empty string if no such prefix exists.

 

Example 1:

Input: s = "level"
Output: "l"
Explanation: s contains 4 prefix excluding itself ("l", "le", "lev", "leve"), and suffix ("l", "el", "vel", "evel"). The largest prefix which is also suffix is given by "l".
Example 2:

Input: s = "ababab"
Output: "abab"
Explanation: "abab" is the largest prefix which is also suffix. They can overlap in the original string.
Example 3:

Input: s = "leetcodeleet"
Output: "leet"
Example 4:

Input: s = "a"
Output: ""
 

Constraints:

1 <= s.length <= 10^5
s contains only lowercase English letters.
'''
class Solution:
    def longestPrefix(self, s):
        PRIME=1000000007
        prefixHash = 0
        suffixHash = 0
        max_i = 0
        for i in range(len(s) - 1):
            prefixHash = (prefixHash * 26 + (ord(s[i]) - ord('A'))) % PRIME
            p = pow(26, i, PRIME)
            suffixHash = (suffixHash + p * (ord(s[-i-1]) - ord('A'))) % PRIME
            if prefixHash == suffixHash:
                max_i = i + 1
        return s[:max_i]

    def longestPrefix2(self, s):
        i = 0
        j = 1
        array = [0 for _ in range(len(s))]
        while j < len(s):
            if s[i] == s[j]:
                array[j] = i + 1
                i += 1
                j += 1
            elif i == 0:
                array[j] = i
                j += 1
            else:
                i = array[i-1]
        return s[:array[-1]]

s = Solution()
string = "ababab"
# string = "acccbaaacccbaac"
print(s.longestPrefix2(string))
