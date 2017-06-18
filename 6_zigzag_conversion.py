"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
"""
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        result_lst = [[] for _ in xrange(numRows)]
        i = 0
        while (i < len(s) + 2*numRows - 2):
            for j in xrange(numRows):
                if j != 0 and j != numRows - 1 and i-j >= 0 and i-j < len(s):
                    result_lst[j].append(s[i-j])
                if i+j < len(s):
                    result_lst[j].append(s[i+j])
            i += 2*numRows - 2
        #print result_lst
        return ''.join(reduce(lambda x,y: x+y, result_lst))
