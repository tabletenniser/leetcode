'''
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        result = set()
        for i in xrange(len(nums)-3):
            for j in xrange(i+1, len(nums) - 2):
                if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target:
                    break
                l, r = j+1, len(nums) - 1
                cur_sum = nums[i] + nums[j]
                while l < r:
                    real_sum = cur_sum + nums[l] + nums[r]
                    if real_sum == target:
                        result.add((nums[i], nums[j], nums[l], nums[r]))
                        l += 1
                    elif real_sum < target:
                        l += 1
                    else:
                        r -= 1
        return list(result)
