'''
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        L = len(nums)
        hash_set = dict()
        for i in xrange(L):
            hash_set[nums[i]] = i

        result = set()
        for i in xrange(L):
            for j in xrange(i+1, L):
                target = -(nums[i] + nums[j])
                if target in hash_set and hash_set[target] != i and hash_set[target] != j:
                    #print i, j, hash_set[target], target
                    new_triplet = [nums[i], nums[j], target]
                    new_triplet.sort()
                    result.add(tuple(new_triplet))
                if target >= nums[-1]:
                    break
        return list(result)
