'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if c == '(' or c =='{' or c == '[':
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                d = stack[-1]
                del stack[-1]
                if c == ')' and d != '(':
                    return False
                if c == ']' and d != '[':
                    return False
                if c == '}' and d != '{':
                    return False
        if len(stack) == 0:
            return True
        return False
