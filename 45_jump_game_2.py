'''

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)

Note:
You can assume that you can always reach the last index.
'''

class Solution(object):
    def jump_too_slow(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        stepsReq = [999999999 for _ in xrange(len(nums))]
        stepsReq[0] = 0
        for i in xrange(len(nums)):
            n = nums[i]
            for j in xrange(1, n+1):
                if i+j >= len(stepsReq):
                    break
                stepsReq[i+j] = min(stepsReq[i] + 1, stepsReq[i+j])
        return stepsReq[-1]

    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        stepsReq = [-1 for _ in xrange(len(nums))]
        stepsReq[0] = 0
        i = 0
        curSteps = 0
        furthest = nums[0]
        while stepsReq[-1] == -1:
            nextFurthest = 0
            while i <= furthest and i < len(nums):
                stepsReq[i] = curSteps + 1
                nextFurthest = max(nextFurthest, nums[i] + i)
                i += 1
            curSteps += 1
            furthest = nextFurthest
        return stepsReq[-1]

s = Solution()
print s.jump([2,3,1,1,4])
print s.jump([1, 2, 3])
print s.jump([0])
