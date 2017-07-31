'''

Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.
'''
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        result = []
        while num > 0:
            if num >= 1000:
                result.append('M')
                num -= 1000
            elif num >= 900: 
                result.append('CM')
                num -= 900
            elif num >= 500: 
                result.append('D')
                num -= 500
            elif num >= 400:
                result.append('CD')
                num -= 400
            elif num >= 100:
                result.append('C')
                num -= 100
            elif num >= 90:
                result.append('XC')
                num -= 90
            elif num >= 50:
                result.append('L')
                num -= 50
            elif num >= 40:
                result.append('XL')
                num -= 40
            elif num >= 10:
                result.append('X')
                num -= 10
            elif num >= 9:
                result.append('IX')
                num -= 9
            elif num >= 5:
                result.append('V')
                num -= 5
            elif num >= 4:
                result.append('IV')
                num -= 4
            else:
                result.append('I')
                num -= 1
        return ''.join(result)
