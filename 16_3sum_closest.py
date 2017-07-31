'''
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        result = 0
        min_diff = 999999999999
        for i in xrange(len(nums) - 2):
            l, r = i+1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                # t = nums[i] + nums[l] + nums[l + 1]
                if s > target:
                    diff = s - target
                    r -= 1
                elif s == target:
                    return s
                else:
                    diff = target - s
                    l += 1
                if diff < min_diff:
                    min_diff = diff
                    result = s
                # if t > target:
                #     if t - target < min_diff:
                #         min_diff = t - target
                #         result = t
                #     break
        return result
