'''

Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.
2:abc
3:def
...
8:tuv
9:wxyz

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.

'''
class Solution(object):
    def generate_strs(self, lst_in, cur_str, result):
        cur_index = len(cur_str)
        if len(lst_in) == cur_index:
            if cur_index != 0:
                result.append(cur_str)
            return
        for c in lst_in[cur_index]:
            self.generate_strs(lst_in, cur_str+c, result)
        return
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        hash_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        recurse_in = []
        for d in digits:
            recurse_in.append(hash_map[d])
        #print recurse_in

        result = []
        self.generate_strs(recurse_in, '', result)
        return result
