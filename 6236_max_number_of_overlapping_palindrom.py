'''
You are given a string s and a positive integer k.
Select a set of non-overlapping substrings from the string s that satisfy the following conditions:
The length of each substring is at least k.
Each substring is a palindrome.
Return the maximum number of substrings in an optimal selection.
A substring is a contiguous sequence of characters within a string.

Example 1:

Input: s = "abaccdbbd", k = 3
Output: 2
Explanation: We can select the substrings underlined in s = "abaccdbbd". Both "aba" and "dbbd" are palindromes and have a length of at least k = 3.
It can be shown that we cannot find a selection with more than two valid substrings.
Example 2:
Input: s = "adbcda", k = 2
Output: 0
Explanation: There is no palindrome substring of length at least 2 in the string.

Constraints:
1 <= k <= s.length <= 2000
s consists of lowercase English letters.
'''
class Solution:
    def isPalingdrome(self, array, string, index, min_len):
        i = 0
        while i < min_len:
            if index + i >= len(string):
                return False
            if string[index + i] != array[-i - 1]:
                return False
            i += 1
        # print(f'is Palingdrom!: {array} {string[index-min_len:index+min_len]}')
        return True

    def maxPalindromes(self, s: str, k: int) -> int:
        if k == 1:
            return len(s)
        i = 0
        stack = []
        res = 0
        while i < len(s):
            # print(s, i, stack, s[i])
            if len(stack) * 2 >= k and self.isPalingdrome(stack, s, i, (k +1)//2):
                i = i + k // 2
                stack = []
                res += 1
                continue
            if len(stack) * 2 - 1 >= k and self.isPalingdrome(stack[:-1], s, i, k // 2):
                i = i + k // 2
                stack = []
                res += 1
                continue
            stack.append(s[i])
            i += 1
        return res

sol = Solution()
s = "abaccdbbd"
k = 3
# s = "iqqibcecvrbxxj"
# k = 1
# s = "gataghmwwmoeyeov"
# k = 4
# s = "sjbxiufnaanqkwsqswkqrcznzcddhtuhtthuttjfuufjtcfywgecegwyhhnnhtozczirynhhnyrire"
# k = 3
print(s)
print(sol.maxPalindromes(s, k))
