"""
Given an array consists of non-negative integers, your task is to count the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.

Example 1:
    Input: [2,2,3,4]
    Output: 3
    Explanation:
        Valid combinations are: 
            2,3,4 (using the first 2)
            2,3,4 (using the second 2)
            2,2,3
Note:
    The length of the given array won't exceed 1000.
    The integers in the given array are in the range of [0, 1000].
"""
class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return 0
        nums.sort()
        result = 0
        l = len(nums)
        for i in xrange(l):
            k = i + 2
            for j in xrange(i+1,l):
                target = nums[i]+nums[j]
                while k < len(nums) and nums[k] < target:
                    k += 1
                new_trig_nums = k - 1 - j 
                if new_trig_nums > 0:
                    result += new_trig_nums
        return result
