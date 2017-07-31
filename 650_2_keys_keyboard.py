'''

Initially on a notepad only one character 'A' is present. You can perform two operations on this notepad for each step:

Copy All: You can copy all the characters present on the notepad (partial copy is not allowed).
Paste: You can paste the characters which are copied last time.
Given a number n. You have to get exactly n 'A' on the notepad by performing the minimum number of steps permitted. Output the minimum number of steps to get n 'A'.

Example 1:
Input: 3
Output: 3
Explanation:
Intitally, we have one character 'A'.
In step 1, we use Copy All operation.
In step 2, we use Paste operation to get 'AA'.
In step 3, we use Paste operation to get 'AAA'.
Note:
The n will be in the range [1, 1000].
'''
class Solution(object):
    def minStepsRecurs(self, target, cur_count, cur_copy):
        #print target,cur_count,cur_copy
        if cur_count == target:
            return 0
        if cur_count > target:
            return 99999999999
        pasteResult, copyResult = 99999999999, 99999999999
        if cur_copy > 0:
            pasteResult = self.minStepsRecurs(target, cur_count+cur_copy, cur_copy)
        if cur_copy < cur_count:
            copyResult = self.minStepsRecurs(target, cur_count, cur_count)
        return min(pasteResult, copyResult) + 1

    def minSteps(self, n):
        return self.minStepsRecurs(n, 1, 0)

    def minSteps2(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0 for _ in xrange(n+1)]
        for i in xrange(2, n+1):
            dp[i] = i
            for j in xrange(i/2, 1, -1):
                if (i % j == 0):
                    dp[i] = dp[j] + i/j
                    break
        return dp[n]
