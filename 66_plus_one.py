'''

Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.

'''
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 0
        for i in xrange(len(digits) - 1, -1, -1):
            if digits[i] + 1 == 10:
                carry = 1
                digits[i] = 0
            else:
                carry = 0
                digits[i] += 1
                break
        if carry == 1:
            digits = [1] + digits
        return digits
