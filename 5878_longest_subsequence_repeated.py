'''
You are given a string s of length n, and an integer k. You are tasked to find the longest subsequence repeated k times in string s.

A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

A subsequence seq is repeated k times in the string s if seq * k is a subsequence of s, where seq * k represents a string constructed by concatenating seq k times.

For example, "bba" is repeated 2 times in the string "bababcba", because the string "bbabba", constructed by concatenating "bba" 2 times, is a subsequence of the string "bababcba".
Return the longest subsequence repeated k times in string s. If multiple such subsequences are found, return the lexicographically largest one. If there is no such subsequence, return an empty string.

 

Example 1:

example 1
Input: s = "letsleetcode", k = 2
Output: "let"
Explanation: There are two longest subsequences repeated 2 times: "let" and "ete".
"let" is the lexicographically largest one.
Example 2:

Input: s = "bb", k = 2
Output: "b"
Explanation: The longest subsequence repeated 2 times is "b".
Example 3:

Input: s = "ab", k = 2
Output: ""
Explanation: There is no subsequence repeated 2 times. Empty string is returned.
Example 4:

Input: s = "bbabbabbbbabaababab", k = 3
Output: "bbbb"
Explanation: The longest subsequence "bbbb" is repeated 3 times in "bbabbabbbbabaababab".
 

Constraints:
n == s.length
2 <= k <= 2000
2 <= n < k * 8
s consists of lowercase English letters.
'''
class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        n = len(s)
        ht = dict()
        for ch in s:
            ht[ch] = ht.get(ch, 0) + 1
        res = ''
        cur_max = 0
        for key,v in ht.items():
            if v > cur_max:
                res = key * (v // k)
                cur_max = v
        print(ht)
        return res

sol = Solution()
s = "bbabbabbbbabaababab"
k = 3
res = sol.longestSubsequenceRepeatedK(s, k)
print(res)
