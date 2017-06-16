"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

    Input: "babad"

    Output: "bab"

    Note: "aba" is also a valid answer.
    Example:

        Input: "cbbd"

        Output: "bb"
"""

class Solution(object):
    def findPalindrome(self, s, mid1, mid2):
        # Odd length
        i = 0
        while (mid1-i >= 0 and mid2+i < len(s) and s[mid1-i] == s[mid2+i]):
            i += 1
        return mid1-i+1, mid2+i

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxLength = 0
        startingIndex = 0
        for i in xrange(len(s)):
            sI, eI = self.findPalindrome(s, i, i)    # For odd length
            if (eI-sI) > maxLength:
                startingIndex, maxLength = sI, (eI-sI)
            sI, eI = self.findPalindrome(s, i, i+1)    # For odd length
            if (eI-sI) > maxLength:
                startingIndex, maxLength = sI, (eI-sI)

        return s[startingIndex:startingIndex+maxLength]

