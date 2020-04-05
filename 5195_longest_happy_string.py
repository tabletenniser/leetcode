'''
A string is called happy if it does not have any of the strings 'aaa', 'bbb' or 'ccc' as a substring.
Given three integers a, b and c, return any string s, which satisfies following conditions:

s is happy and longest possible.
s contains at most a occurrences of the letter 'a', at most b occurrences of the letter 'b' and at most c occurrences of the letter 'c'.
s will only contain 'a', 'b' and 'c' letters.
If there is no such string s return the empty string "".

Example 1:

Input: a = 1, b = 1, c = 7
Output: "ccaccbcc"
Explanation: "ccbccacc" would also be a correct answer.
Example 2:

Input: a = 2, b = 2, c = 1
Output: "aabbc"
Example 3:

Input: a = 7, b = 1, c = 0
Output: "aabaa"
Explanation: It's the only correct answer in this case.

Constraints:

0 <= a, b, c <= 100
a + b + c > 0
'''
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = []
        ca, cb, cc = True, True, True
        while True:
            ca = a > 0 and not (len(res) >= 2 and res[-1] == 'a' and res[-2] == 'a')
            cb = b > 0 and not (len(res) >= 2 and res[-1] == 'b' and res[-2] == 'b')
            cc = c > 0 and not (len(res) >= 2 and res[-1] == 'c' and res[-2] == 'c')
            print(a,b,c,ca,cb,cc, res)
            if ca and (a >= b or not cb) and (a >= c or not cc):
                res.append('a')
                a -= 1
            elif cb and (b >= c or not cc):
                res.append('b')
                b -= 1
            elif cc:
                res.append('c')
                c -= 1
            else:
                break
        return ''.join(res)


s = Solution()
a = 1
b = 1
c = 7
res = s.longestDiverseString(a, b, c)
print(res)

