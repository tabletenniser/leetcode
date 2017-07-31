'''
Write a function to find the longest common prefix string amongst an array of strings.
'''
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        i = 0
        while True:
            if i == len(strs[0]):
                return strs[0][:i]
            ch = strs[0][i]
            for str in strs:
                if i == len(str) or str[i] != ch:
                    return str[:i]
            i += 1
        assert(False)
        return ''
