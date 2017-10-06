'''
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
'''
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        hash_table = dict()
        def nd_rec(string):
            if len(string) == 0 or string[0] == '0':
                return 0
            if len(string) == 1:
                return 1
            if len(string) == 2:
                if int(string) <= 26:
                    return 2 if string != '10' and string != '20' else 1
                else:
                    return 1 if string[1] != '0' else 0
            if string in hash_table:
                return hash_table[string]
            res = nd_rec(string[1:])
            if int(string[:2]) <= 26:
                res += nd_rec(string[2:])
            hash_table[string] = res
            return res
        result = nd_rec(s)
        return result

s = Solution()
print s.numDecodings("12")   # Expect 2
print s.numDecodings("125")   # Expect 3
print s.numDecodings("1225")   # Expect 5
print s.numDecodings("10")   # Expect 1
print s.numDecodings("122225")   # Expect 1
print s.numDecodings("4757562545844617494555774581341211511296816786586787755257741178599337186486723247528324612117156948")   # Expect 1
