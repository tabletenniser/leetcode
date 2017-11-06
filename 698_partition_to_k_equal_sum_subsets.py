'''
Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.

Example 1:
Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
Note:

1 <= k <= len(nums) <= 16.
0 < nums[i] < 10000.
'''
class Solution(object):
    def iterateAllSubstes(self, nums, sums, cur_nums, n):
        if n == len(nums):
            if len(cur_nums) > 0:
                s = sum(cur_nums)
                if s == 55701:
                    print sorted(cur_nums)
                sums[s] = sums.get(s, 0) + 1
            return
        self.iterateAllSubstes(nums, sums, cur_nums, n + 1)
        self.iterateAllSubstes(nums, sums, cur_nums + [nums[n]], n + 1)

    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        sums = dict()
        self.iterateAllSubstes(nums, sums, [], 0)
        # print sums
        for s in sums:
            if sums[s] >= k:
                return True
        return False

s = Solution()
# print s.canPartitionKSubsets([4,3,2,3,5,2,1], 4)
# print s.canPartitionKSubsets([4,3,2,3,5,2,1,2,3,1,5,1,5,21], 4)
# print s.canPartitionKSubsets([1334,4518,1235,1146,3565,64,913,203,1522], 2)
print s.canPartitionKSubsets([7628, 3147, 7137, 2578, 7742, 2746, 4264, 7704, 9532, 9679, 8963, 3223, 2133, 7792, 5911, 3979], 6)
