'''
Given an integer array nums and an integer k, return the maximum sum of a non-empty subset of that array such that for every two consecutive integers in the subset, nums[i] and nums[j], where i < j, the condition j - i <= k is satisfied.
A subset of an array is obtained by deleting some number of elements (can be zero) from the array, leaving the remaining elements in their original order.

Example 1:
Input: nums = [10,2,-10,5,20], k = 2
Output: 37
Explanation: The subset is [10, 2, 5, 20].

Example 2:
Input: nums = [-1,-2,-3], k = 1
Output: -1
Explanation: The subset must be non-empty, so we choose the largest number.

Example 3:
Input: nums = [10,-2,-10,-5,20], k = 2
Output: 23
Explanation: The subset is [10, -2, -5, 20].

Constraints:
1 <= k <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
'''
import sys
sys.setrecursionlimit(100000)
class Solution:
    def max_sum(self, nums, l, h, k):
        cur_max = -99999999999999999999999999999
        for k_i in range(k):
            cur_sum = 0
            for n in range(l+k_i, h+1, k):
                cur_sum += nums[n]
            cur_max = max(cur_sum, cur_max)
        return cur_max

    def constrainedSubsetSum(self, nums, k) -> int:
        if max(nums) < 0:
            return max(nums)
        res = 0
        n_start = None
        for i in range(len(nums)):
            num = nums[i]
            if num >= 0:
                if n_start:
                    if n_start != 0:
                        n_range_sum = self.max_sum(nums, n_start, i - 1, k)
                        res = max(0, res + n_range_sum)
                    n_start = None
                res += num
            else:
                if not n_start:
                    n_start = i
        return res

    def rec(self, cur_ind, cur_k):
        if (cur_ind, cur_k) in self.ht:
            return self.ht[(cur_ind, cur_k)]
        if cur_ind == 0:
            return max(0, self.nums[cur_ind]) if cur_k < self.k else self.nums[cur_ind]
        choose = self.rec(cur_ind - 1, 1) + self.nums[cur_ind]
        res = choose
        if cur_k < self.k and self.nums[cur_ind] < 0:
            not_choose = self.rec(cur_ind - 1, cur_k + 1)
            res = max(res, not_choose)
        # print(cur_ind, cur_k, res)
        self.ht[(cur_ind, cur_k)] = res
        return res

    def constrainedSubsetSum2(self, nums, k) -> int:
        if max(nums) < 0:
            return max(nums)
        self.nums = nums
        self.k = k
        self.ht = dict()
        return self.rec(len(nums)-1, 1)

s = Solution()
# nums = [10,-2,-10,-5,20]
# k = 2
# nums = [-1,-2,-3]
# k = 1
# nums =[-5266,4019,7336,-3681,-5767]
# k = 2
nums = [-8269,3217,-4023,-4138,-683,6455,-3621,9242,4015,-3790]
k = 1
# nums = [(-1)**i * i for i in range(10000)]
# k = 5000
res = s.constrainedSubsetSum(nums, k)
print(res)
