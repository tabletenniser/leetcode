'''
In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", a move consists of either replacing one occurrence of "XL" with "LX", or replacing one occurrence of "RX" with "XR". Given the starting string start and the ending string end, return True if and only if there exists a sequence of moves to transform one string to the other.

Example:

Input: start = "RXXLRXRXL", end = "XRLXXRRLX"
Output: True
Explanation:
We can transform start to end following these steps:
RXXLRXRXL ->
XRXLRXRXL ->
XRLXRXRXL ->
XRLXXRRXL ->
XRLXXRRLX
Note:

1 <= len(start) = len(end) <= 10000.
Both start and end will only consist of characters in {'L', 'R', 'X'}.
'''
class Solution(object):
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        strings = set()
        def try_all_permutation(string):
            if string == end:
                return True
            if string in strings:
                return False
            strings.add(string)
            print string
            for i in xrange(len(string)-1):
                if string[i:i+2] == 'XL':
                    new_str = string[:i]+'LX'+string[i+2:]
                    if new_str not in strings and try_all_permutation(new_str):
                        return True
                if string[i:i+2] == 'RX':
                    new_str = string[:i]+'XR'+string[i+2:]
                    if new_str not in strings and try_all_permutation(new_str):
                        return True
            return False
        return try_all_permutation(start)

s = Solution()
start = "XXRXXLXXLLRXXLXXLXLXRXXLXXRXRX"
end   = "XRXLXXXXLLXXXRLLLXRXXLRXXXXXRX"
assert s.canTransform(start, end)

