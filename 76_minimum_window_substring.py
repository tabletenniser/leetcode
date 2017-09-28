'''

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the empty string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.

'''
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        hashmap = dict()
        for ch in t:
            hashmap[ch] = hashmap.get(ch, 0) + 1
        i, j = 0, 0
        res = ""
        cur_len = 9999999999
        unmatched_ch_len = len(t)
        while j <= len(s) and i < len(s):
            if j < len(s) and unmatched_ch_len > 0:
                if s[j] in hashmap:
                    if hashmap[s[j]] > 0:
                        unmatched_ch_len -= 1
                    hashmap[s[j]] -= 1
                j += 1
            else:
                # Current substring is valid
                if unmatched_ch_len == 0 and j - i + 1 < cur_len:
                    cur_len = j - i + 1
                    res = s[i:j]
                if s[i] in hashmap:
                    hashmap[s[i]] += 1
                    if hashmap[s[i]] > 0:
                        unmatched_ch_len += 1
                i += 1
        return res

s = Solution()
print s.minWindow("", "")
print s.minWindow("ADOBECODEBANC", "ABC")
