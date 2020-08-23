'''
Given an array of integers nums and an integer target.
Return the number of non-empty subsequences of nums such that the sum of the minimum and maximum element on it is less or equal than target.
Since the answer may be too large, return it modulo 10^9 + 7.

Example 1:
Input: nums = [3,5,6,7], target = 9
Output: 4
Explanation: There are 4 subsequences that satisfy the condition.
[3] -> Min value + max value <= target (3 + 3 <= 9)
[3,5] -> (3 + 5 <= 9)
[3,5,6] -> (3 + 6 <= 9)
[3,6] -> (3 + 6 <= 9)

Example 2:
Input: nums = [3,3,6,8], target = 10
Output: 6
Explanation: There are 6 subsequences that satisfy the condition. (nums can have repeated numbers).
[3] , [3] , [3,3], [3,6] , [3,6] , [3,3,6]

Example 3:
Input: nums = [2,3,3,4,6,7], target = 12
Output: 61
Explanation: There are 63 non-empty subsequences, two of them don't satisfy the condition ([6,7], [7]).
Number of valid subsequences (63 - 2 = 61).

Example 4:
Input: nums = [5,2,4,1,7,6,8], target = 16
Output: 127
Explanation: All non-empty subset satisfy the condition (2^7 - 1) = 127

Constraints:
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^6
1 <= target <= 10^6
'''
from bisect import bisect_right

class Solution:
    def numSubseq2(self, nums, target: int) -> int:
        nums.sort()
        n = len(nums)
        res = 2 ** n - 1
        for i, num in enumerate(nums):
            j = bisect_right(nums, target-num, i, n)
            if j < n:
                j = max(i, j)
                middle = 2**(j-1-i) if j >= i+1 else 1
                if i == j:
                    right = 2 ** (n-j-1)
                else:
                    right = 2 ** (n-j) - 1
                res -= middle * right
                # print(middle, right,res)
            # print(i,j,':',num,nums[j] if j < n else -1,res)
        return res % (1000000007)

    def numSubseq(self, nums, target: int) -> int:
        res = 0
        nums.sort()
        n = len(nums)
        i, j = 0, n - 1
        while i < n:
            while nums[i] + nums[j] > target:
                j -= 1
            if j < i:
                break
            res += 2 ** (j-i)
            # print(i,j,res)
            i += 1
        return res


s = Solution()
nums = [2,3,3,4,6,7]
target = 12
nums = [3,3,6,8]
target = 10
nums = [3,5,6,7]
target = 9
nums = [5,2,4,1,7,6,8]
target = 16
nums = [1, 1, 2, 3, 4, 6, 9, 9]
target = 6
print(s.numSubseq(nums, target))
