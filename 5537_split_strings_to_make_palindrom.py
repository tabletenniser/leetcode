'''
You are given two strings a and b of the same length. Choose an index and split both strings at the same index, splitting a into two strings: aprefix and asuffix where a = aprefix + asuffix, and splitting b into two strings: bprefix and bsuffix where b = bprefix + bsuffix. Check if aprefix + bsuffix or bprefix + asuffix forms a palindrome.

When you split a string s into sprefix and ssuffix, either ssuffix or sprefix is allowed to be empty. For example, if s = "abc", then "" + "abc", "a" + "bc", "ab" + "c" , and "abc" + "" are valid splits.

Return true if it is possible to form a palindrome string, otherwise return false.

Notice that x + y denotes the concatenation of strings x and y.

Example 1:

Input: a = "x", b = "y"
Output: true
Explaination: If either a or b are palindromes the answer is true since you can split in the following way:
aprefix = "", asuffix = "x"
bprefix = "", bsuffix = "y"
Then, aprefix + bsuffix = "" + "y" = "y", which is a palindrome.
Example 2:

Input: a = "abdef", b = "fecab"
Output: false
Example 3:

Input: a = "ulacfd", b = "jizalu"
Output: true
Explaination: Split them at index 3:
aprefix = "ula", asuffix = "cfd"
bprefix = "jiz", bsuffix = "alu"
Then, aprefix + bsuffix = "ula" + "alu" = "ulaalu", which is a palindrome.
'''
class Solution:
    def isP(self, string):
        n = len(string)
        i = 0
        while i < n / 2:
            if string[i] != string[n - 1 - i]:
                # print(string,False)
                return False
            i += 1
        # print(string,True)
        return True

    def check(self, a: str, b: str) -> bool:
        i = 0
        n = len(b)
        while i < n / 2:
            # print(a[i], b[n-1-i])
            if a[i] != b[n - 1 - i]:
                if self.isP(a[:i]+b[i:]) or self.isP(a[:n-i]+b[n-i:]):
                    return True
                else:
                    return False
            i += 1
        return True

    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        return self.check(a,b) or self.check(b,a)

sol = Solution()
a = "ulacfd"
b = "jizalu"
a = "abcba"
b = "pnmdz"
a = "abcdba"
b = "abfoop"
print(sol.checkPalindromeFormation(a, b))
