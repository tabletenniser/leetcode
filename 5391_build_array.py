'''
Given three integers n, m and k. Consider the following algorithm to find the maximum element of an array of positive integers:

You should build the array arr which has the following properties:
- arr has exactly n integers.
- 1 <= arr[i] <= m where (0 <= i < n).
- After applying the mentioned algorithm to arr, the value search_cost is equal to k.
Return the number of ways to build the array arr under the mentioned conditions. As the answer may grow large, the answer must be computed modulo 10^9 + 7.

Example 1:
Input: n = 2, m = 3, k = 1
Output: 6
Explanation: The possible arrays are [1, 1], [2, 1], [2, 2], [3, 1], [3, 2] [3, 3]

Example 2:
Input: n = 5, m = 2, k = 3
Output: 0
Explanation: There are no possible arrays that satisify the mentioned conditions.

Example 3:
Input: n = 9, m = 1, k = 1
Output: 1
Explanation: The only possible array is [1, 1, 1, 1, 1, 1, 1, 1, 1]

Example 4:
Input: n = 50, m = 100, k = 25
Output: 34549172
Explanation: Don't forget to compute the answer modulo 1000000007

Example 5:
Input: n = 37, m = 17, k = 7
Output: 418930126

Constraints:

1 <= n <= 50
1 <= m <= 100
0 <= k <= n
'''
class Solution:
    def sc(self, arr):
        max_val = -1
        sc = 0
        for elem in arr:
            if elem > max_val:
                max_val = elem
                sc += 1
        return sc

    def rec(self, n, max_num, m, k):
        if (n,max_num,k) in self.ht:
            return self.ht[(n,max_num,k)]
        if n == 0:
            return 1 if k == 0 else 0
        res = 0
        for num in range(1, m+1):
            if num > max_num:
                res += self.rec(n - 1, num, m, k - 1)
            else:
                res += self.rec(n - 1, max_num, m, k)
        self.ht[(n, max_num, k)] = res
        return res

    def numOfArrays(self, n: int, m: int, k: int) -> int:
        self.ht = dict()
        return self.rec(n, 0, m, k) % 1000000007

s = Solution()
# n = 5
# m = 2
# k = 3
n = 50
m = 100
k = 25
res = s.numOfArrays(n, m, k)
print(res)

