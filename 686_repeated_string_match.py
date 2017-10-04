'''
Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution, return -1.

For example, with A = "abcd" and B = "cdabcdab".

Return 3, because by repeating A three times ("abcdabcdabcd"), B is a substring of it; and B is not a substring of A repeated two times ("abcdabcd").

Note:
The length of A and B will be between 1 and 10000.
'''
class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        i = 1
        while len(A) * i <= len(B) + len(A) * 2:
            if len(A) * i >= len(B):
                copy_A = A*i
                print copy_A, B, copy_A.find(B)
                if copy_A.find(B) >= 0:
                    return i
            i += 1
        return -1
        # if len(B) == 0:
        #     return 1 if len(A) == 0 else -1
        # ch = B[0]
        # i = 0
        # while i < len(A):
        #     if A[i] == ch:
        #         break
        #     i += 1
        # if i == len(A):
        #     return -1
        #
        # j = 0
        # while j < len(B):
        #     if A[(i + j) % len(A)] != B[j]:
        #         return -1
        #     j += 1
        # res = len(B) / len(A) + 1
        # if i == 0 and (i+j) % len(A) == 0:
        #     res -= 1
        # return res

s = Solution()
print s.repeatedStringMatch("abababaaba", "aabaaba")
print s.repeatedStringMatch("ab", "ab")
print s.repeatedStringMatch("ab", "aba")
print s.repeatedStringMatch("ab", "bab")
print s.repeatedStringMatch("ab", "abab")
print s.repeatedStringMatch("ab", "abababa")
print s.repeatedStringMatch("a", "aa")
print s.repeatedStringMatch("a", "a")
