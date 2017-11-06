'''
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:
Input: [1, 2, 2, 3, 1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
Example 2:
Input: [1,2,2,3,1,4,2]
Output: 6
Note:

nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.
'''
class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        frequency = dict()
        start = dict()
        end = dict()
        for i in xrange(len(nums)):
            n = nums[i]
            frequency[n] = frequency.get(n, 0) + 1
            if n not in start:
                start[n] = i
            end[n] = i

        max_occ = 0
        max_n = []
        for key in frequency:
            value = frequency[key]
            if value > max_occ:
                max_n = [key]
                max_occ = value
            elif value == max_occ:
                max_n.append(key)

        res = len(nums)
        for m in max_n:
            res = min(res, end[m]-start[m]+1)
        return res


s = Solution()
print s.findShortestSubArray([1,2,2,3,1])
print s.findShortestSubArray([1,2,2,3,1,4,2])
print s.findShortestSubArray([1])
