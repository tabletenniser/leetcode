'''
You are given two strings, word1 and word2. You want to construct a string in the following manner:
Choose some non-empty subsequence subsequence1 from word1.
Choose some non-empty subsequence subsequence2 from word2.
Concatenate the subsequences: subsequence1 + subsequence2, to make the string.
Return the length of the longest palindrome that can be constructed in the described manner. If no palindromes can be constructed, return 0.
A subsequence of a string s is a string that can be made by deleting some (possibly none) characters from s without changing the order of the remaining characters.
A palindrome is a string that reads the same forward as well as backward.

Example 1:
Input: word1 = "cacb", word2 = "cbba"
Output: 5
Explanation: Choose "ab" from word1 and "cba" from word2 to make "abcba", which is a palindrome.

Example 2:
Input: word1 = "ab", word2 = "ab"
Output: 3
Explanation: Choose "ab" from word1 and "a" from word2 to make "aba", which is a palindrome.

Example 3:
Input: word1 = "aa", word2 = "bb"
Output: 0
Explanation: You cannot construct a palindrome from the described method, so return 0.

Constraints:
1 <= word1.length, word2.length <= 1000
word1 and word2 consist of lowercase English letters.
'''
class Solution:
    def MCS(self, w1, w2):
        l1, l2 = len(w1), len(w2)
        dp = [[0 for _ in range(l2+1)] for _ in range(l1+1)]
        print(w1,w2,l1,l2)
        from_last_digit = False
        for i in range(1,l1+1):
            for j in range(1, l2+1):
                from_last_digit = False
                if w1[i-1] == w2[j-1]:
                    dp[i][j] = max(dp[i-1][j-1]+1, dp[i][j-1], dp[i-1][j])
                    if dp[i][j] > dp[i][j-1] and dp[i][j] > dp[i-1][j]:
                        from_last_digit = True
                else:
                    dp[i][j] = max(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])
        # for row in dp:
        #     print(row)
        return dp, from_last_digit

    def sub(self, w1, w2):
        dp, from_last_digit = self.MCS(w1, w2)
        res = 2 * dp[-1][-1]
        if res > 0 and (not from_last_digit):
            res += 1
        return res

    def longestPalindrome(self, w1, w2):
        return max(self.sub(w1,w2[::-1]), self.sub(w1[::-1], w2))


w1 = "cacb"
w2 = "cbbaz"
w1 = "ab"
w2 = "a"
s = Solution()
print(s.longestPalindrome(w1, w2))
