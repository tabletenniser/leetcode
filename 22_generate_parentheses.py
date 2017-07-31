'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''
class Solution(object):
    def gpRec(self, n_left, n_right, cur_str, result):
        if n_left == 0 and n_right == 0:
            result.append(cur_str)
            return
        if n_left > 0:
            self.gpRec(n_left-1, n_right, cur_str+'(', result)
        if n_right > n_left and n_right > 0:
            self.gpRec(n_left, n_right-1, cur_str+')', result)
        return

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        self.gpRec(n, n, '', result)
        return result
