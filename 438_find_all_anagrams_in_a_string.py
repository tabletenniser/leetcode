'''
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
'''
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        char_map = dict()
        for ch in p:
            char_map[ch] = char_map.get(ch, 0) + 1

        result = []
        for i in xrange(len(s)):
            ch = s[i]
            char_map[ch] = char_map.get(ch, 0) - 1
            if char_map[ch] == 0:
                del char_map[ch]
            if i >= len(p):
                old_ch = s[i-len(p)]
                char_map[old_ch] = char_map.get(old_ch, 0) + 1
                if char_map[old_ch] == 0:
                    del char_map[old_ch]
            if len(char_map) == 0:
                result.append(i-len(p)+1)
        # print result, char_map
        return result

s = Solution()
string="cbaebabacd"
p="abc"
assert s.findAnagrams(string, p) == [0, 6]

assert s.findAnagrams("abab", "ab") == [0, 1, 2]
