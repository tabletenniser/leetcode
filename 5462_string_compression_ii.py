'''
Run-length encoding is a string compression method that works by replacing consecutive identical characters (repeated 2 or more times) with the concatenation of the character and the number marking the count of the characters (length of the run). For example, to compress the string "aabccc" we replace "aa" by "a2" and replace "ccc" by "c3". Thus the compressed string becomes "a2bc3".

Notice that in this problem, we are not adding '1' after single characters.

Given a string s and an integer k. You need to delete at most k characters from s such that the run-length encoded version of s has minimum length.

Find the minimum length of the run-length encoded version of s after deleting at most k characters.


Example 1:
Input: s = "aaabcccd", k = 2
Output: 4
Explanation: Compressing s without deleting anything will give us "a3bc3d" of length 6. Deleting any of the characters 'a' or 'c' would at most decrease the length of the compressed string to 5, for instance delete 2 'a' then we will have s = "abcccd" which compressed is abc3d. Therefore, the optimal way is to delete 'b' and 'd', then the compressed version of s will be "a3c3" of length 4.
Example 2:

Input: s = "aabbaa", k = 2
Output: 2
Explanation: If we delete both 'b' characters, the resulting compressed string would be "a4" of length 2.
Example 3:

Input: s = "aaaaaaaaaaa", k = 0
Output: 3
Explanation: Since k is zero, we cannot delete anything. The compressed string is "a11" of length 3.


Constraints:

1 <= s.length <= 100
0 <= k <= s.length
s contains only lowercase English letters.
'''
class Solution:
    def runTimeLength(self, s):
        c = 0
        prev = None
        res = ''
        for ch in s:
            if ch == prev or prev is None:
                c += 1
            elif prev is not None:
                res += prev
                if c != 1:
                    res += str(c)
                c = 1
            prev = ch
        if c > 0:
            res += prev
            if c != 1:
                res += str(c)
        print(res)
        return ''.join(res)

    def unify(self, s):
        ht = dict()
        res = []
        cur = 0
        for ch in s:
            if ch in ht:
                res.append(ht[ch])
            else:
                ht[ch] = chr(65+cur)
                res.append(ht[ch])
                cur += 1
        return ''.join(res)

    def rec(self, s, k):
        s = self.unify(s)
        print(s,k)
        if (s,k) in self.ht:
            return self.ht[(s,k)]
        if k == 0:
            rtl = self.runTimeLength(s)
            return len(rtl)
        prev = None
        j = 0
        rtl = self.runTimeLength(s)
        res = len(rtl)
        for i, ch in enumerate(s+']'):
            if ch == prev or prev is None:
                pass
            else:
                remaining_k = k - (i - j)
                if remaining_k >= 0:
                    cut_string = s[:j] + s[i:]
                    # print(remaining_k, cut_string)
                    cur = self.rec(cut_string, remaining_k)
                    res = min(res, cur)
                if i - j >= 10:
                    remaining_k = k - (i - j - 9)
                    if remaining_k >= 0:
                        cut_string = s[:j+9] + s[i:]
                        cur = self.rec(cut_string, remaining_k)
                        res = min(res, cur)
                j = i
            prev = ch
        self.ht[(s,k)] = res
        return res

    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        self.ht = dict()
        return self.rec(s, k)


s = "aaabcccd"
k = 2
s = "aabbaa"
k = 2
s = "aaaaaaaaaaa"
k = 0
s = "abc"
k = 2
s = "llllllllllttttttttt"
k = 1
# s = "abcdefghijklmnopqrstuvwxyz"
# k = 16
s = "ccacbaacabaabbcaccbabccacbbac"
k = 9
sol = Solution()
print(sol.getLengthOfOptimalCompression(s, k))
