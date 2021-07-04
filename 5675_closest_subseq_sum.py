'''
You are given an integer array nums and an integer goal.
You want to choose a subsequence of nums such that the sum of its elements is the closest possible to goal. That is, if the sum of the subsequence's elements is sum, then you want to minimize the absolute difference abs(sum - goal).
Return the minimum possible value of abs(sum - goal).
Note that a subsequence of an array is an array formed by removing some elements (possibly all or none) of the original array.

Example 1:
Input: nums = [5,-7,3,5], goal = 6
Output: 0
Explanation: Choose the whole array as a subsequence, with a sum of 6.
This is equal to the goal, so the absolute difference is 0.

Example 2:
Input: nums = [7,-9,15,-2], goal = -5
Output: 1
Explanation: Choose the subsequence [7,-9,-2], with a sum of -4.
The absolute difference is abs(-4 - (-5)) = abs(1) = 1, which is the minimum.

Example 3:
Input: nums = [1,2,3], goal = -7
Output: 7

Constraints:
1 <= nums.length <= 40
-107 <= nums[i] <= 107
-109 <= goal <= 109
'''
import itertools
class Solution:
    def minAbsDifferencePrev(self, nums, goal: int) -> int:
        ps = [0] + list(itertools.accumulate(nums))
        res = abs(goal)
        print(ps)
        for i in range(len(ps)):
            for j in range(i, len(ps)):
                diff = ps[j] - ps[i]
                res = min(abs(diff - goal), res)
        return res

    def rec(self, nums, goal):
        print(nums,goal)
        if len(nums) == 0:
            return abs(goal)
        self.c += 1
        res = self.rec(nums[1:], goal)
        res = min(res, self.rec(nums[1:], goal-nums[0]))
        return res
    def minAbsDifference(self, nums, goal: int) -> int:
        self.c = 0
        mini, maxi = goal, goal
        res = self.rec(nums, goal)
        print("Count:", self.c)
        return res


s = Solution()
nums = [5,-7,3,5]
goal = 6
nums = [7,-9,15,-2]
goal = 5
nums = [7,-9,15,-2]
goal = -5
nums=[3346,-3402,-9729,7432,2475,6852,5960,-7497,3229,6713,8949,9156,3945,-8686,1528,5022,-9791,-3782,-191,-9820,7720,-6067,-83,6793,340,7793,8742,8067]
goal=-20357
print(s.minAbsDifference(nums, goal))
