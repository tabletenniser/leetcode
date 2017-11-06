'''
Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
'''
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start, end = -1, -1

        # Binary search for left boundary
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) / 2
            if nums[mid] == target and (mid == 0 or nums[mid-1] < target):
                start = mid
                break
            elif target <= nums[mid]:
                r = mid - 1
            else:
                l = mid + 1

        # Binary search for right boundary
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) / 2
            if nums[mid] == target and (mid == len(nums) - 1 or nums[mid+1] > target):
                end = mid
                break
            elif target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1

        return [start, end]

s = Solution()
print s.searchRange([5,7,7,8,8,10], 8)  # expects [3,4]
print s.searchRange([5,7,7,8,8,10], 6)  # expects [-1,-1]
print s.searchRange([5,7,7,8,8,10], 5)  # expects [0,0]
print s.searchRange([5,7,7,8,8,10], 10)  # expects [5,5]
