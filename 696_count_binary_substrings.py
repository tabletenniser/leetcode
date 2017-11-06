'''
Give a string s, count the number of non-empty (contiguous) substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.

Example 1:
Input: "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".

Notice that some of these substrings repeat and are counted the number of times they occur.

Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
Example 2:
Input: "10101"
Output: 4
Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.
Note:

s.length will be between 1 and 50,000.
s will only consist of "0" or "1" characters.
'''
class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ones = 0
        zeros = 0
        cur_is_one = False
        res = 0
        for i in xrange(len(s)):
            ch = s[i]
            if ch == '0':
                if cur_is_one == False or i == 0:
                    zeros += 1
                else:
                    zeros = 1
                cur_is_one = False
                if zeros <= ones:
                    res += 1
            elif ch == '1':
                if cur_is_one == True or i == 0:
                    ones += 1
                else:
                    ones = 1
                cur_is_one = True
                if ones <= zeros:
                    res += 1
            else:
                assert(False)
            # print i, zeros, ones
        return res



s = Solution()
print s.countBinarySubstrings("00110011") #expects 6
print s.countBinarySubstrings("10101")    #expects 4
print s.countBinarySubstrings("1")    #expects 0
print s.countBinarySubstrings("01")    #expects 1
print s.countBinarySubstrings("101")    #expects 2
