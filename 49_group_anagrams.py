'''
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
Return:

    [
      ["ate", "eat","tea"],
      ["nat","tan"],
      ["bat"]
    ]
Note: All inputs will be in lower-case.
'''
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result_dic = dict()
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s in result_dic:
                result_dic[sorted_s].append(s)
            else:
                result_dic[sorted_s] = [s]
        return [ v for v in result_dic.values() ]
