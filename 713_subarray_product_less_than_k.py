'''
Your are given an array of positive integers nums.

Count and print the number of (contiguous) subarrays where the product of all the elements in the subarray is less than k.

Example 1:
Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
Note:

0 < nums.length <= 50000.
0 < nums[i] < 1000.
0 <= k < 10^6.
'''
class Solution(object):
    def _count_sub_array(self, n):
        return n*(n+1)/2

    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        cur_product = 1
        result = 0
        l, r = 0, 0
        while (r < len(nums) or cur_product >= k) and l < len(nums):
            if cur_product >= k:
                cur_product /= nums[l]
                l += 1
            else:
                result += r-l
                cur_product *= nums[r]
                r += 1
        if cur_product < k:
            result += r-l
        return result

s = Solution()
print s.numSubarrayProductLessThanK([10,5,2,6], 100)
print s.numSubarrayProductLessThanK([1,1,1,1,1], 100)
print s.numSubarrayProductLessThanK([1,1,1,1,1], 0)
print s.numSubarrayProductLessThanK([1,2,3,4,5], 7) #5+[1,2]+[2,3]+[1,2,3]
print s.numSubarrayProductLessThanK([1], 0)
