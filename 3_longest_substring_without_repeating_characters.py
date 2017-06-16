"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

    Given "abcabcbb", the answer is "abc", which the length is 3.

    Given "bbbbb", the answer is "b", with the length of 1.

    Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
import Queue as Q

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        #unique_chars = set()
        last_index = dict()
        i,j = 0,0

        while j < len(s):
            ch = s[j]
            if ch in last_index:
                i = max(last_index[ch], i)
            last_index[ch] = j + 1
            if j - i + 1 > result:
                result = j - i + 1

            # if ch in unique_chars:
            #     while True:
            #         unique_chars.remove(s[i])
            #         if s[i] == ch:
            #             i += 1
            #             break
            #         i += 1
            # unique_chars.add(ch)
            # if len(unique_chars) > result:
            #     result = len(unique_chars)
            j += 1

        return result
