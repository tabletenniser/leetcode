"""
Determine whether an integer is a palindrome. Do this without extra space.

Some hints:
    Could negative integers be palindromes? (ie, -1)

    If you are thinking of converting the integer to string, note the restriction of using extra space.

    You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

    There is a more generic way of solving this problem.
"""
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        reverse = 0
        original_x = x
        while True:
            reverse += x % 10
            x /= 10
            if x == 0:
                break
            reverse *= 10
        return reverse == original_x
