'''

Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character
'''
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp = [[99999 for _ in xrange(len(word2)+1)] for _ in xrange(len(word1)+1)]
        dp[0][0] = 0
        for i in xrange(len(word1)+1):
            dp[i][0] = i
        for j in xrange(len(word2)+1):
            dp[0][j] = j

        for i in xrange(1, len(word1)+1):
            for j in xrange(1, len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1][j-1])
                else:
                    dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1][j-1] + 1)
        return dp[-1][-1]

s = Solution()
print s.minDistance("abc", "a")
print s.minDistance("a", "abc")
print s.minDistance("", "")
print s.minDistance("", "a")
print s.minDistance("a", "")
print s.minDistance("abcde", "abcde")
print s.minDistance("abcde", "abdde")
print s.minDistance("abcde", "acde")
print s.minDistance("acde", "abcde")
