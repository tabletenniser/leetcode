'''
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
'''
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry = 0
        i, j = len(a) - 1, len(b) - 1
        res = []
        while i >= 0 or j >= 0:
            s = int(a[i]) if i >= 0 else 0
            s += int(b[j]) if j >= 0 else 0
            s += carry
            if s > 1:
                carry = 1
            else:
                carry = 0
            res.insert(0, str(s % 2))
            i -= 1
            j -= 1

        if carry == 1:
            res.insert(0, '1')
        return ''.join(res)
