'''
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
'''
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        mapping = dict()
        mapping['IV'] = 4
        mapping['IX'] = 9
        mapping['XL'] = 40
        mapping['XC'] = 90
        mapping['CD'] = 400
        mapping['CM'] = 900
        single_mapping = dict()
        single_mapping['I'] = 1
        single_mapping['V'] = 5
        single_mapping['X'] = 10
        single_mapping['L'] = 50
        single_mapping['C'] = 100
        single_mapping['D'] = 500
        single_mapping['M'] = 1000

        result = 0
        i = 0
        L = len(s)
        while i < L:
            if i+2 <= L and s[i:i+2] in mapping:
                result += mapping[s[i:i+2]]
                i += 2
            else:
                result += single_mapping[s[i]]
                i += 1
        return result
