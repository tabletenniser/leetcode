'''
You are given an array nums and an integer k. The XOR of a segment [left, right] where left <= right is the XOR of all the elements with indices between left and right, inclusive: nums[left] XOR nums[left+1] XOR ... XOR nums[right].

Return the minimum number of elements to change in the array such that the XOR of all segments of size k is equal to zero.
Input: nums = [1,2,0,3,0], k = 1
Output: 3
Explanation: Modify the array from [1,2,0,3,0] to from [0,0,0,0,0].
Example 2:
Input: nums = [3,4,5,2,1,7,3,4,7], k = 3
Output: 3
Explanation: Modify the array from [3,4,5,2,1,7,3,4,7] to [3,4,7,3,4,7,3,4,7].
Example 3:
Input: nums = [1,2,4,1,2,5,1,2,6], k = 3
Output: 3
Explanation: Modify the array from [1,2,4,1,2,5,1,2,6] to [1,2,3,1,2,3,1,2,3].

Constraints:
1 <= k <= nums.length <= 2000
0 <= nums[i] < 210
'''
class Solution:
    def minChanges_bad(self, nums, k: int) -> int:
        cur_xor = 0
        i = 0
        while i < k-1:
            cur_xor = cur_xor ^ nums[i]
            i += 1
        res = 0
        while i < len(nums):
            # print(i, nums[i], cur_xor)
            if cur_xor != nums[i]:
                nums[i] = cur_xor
                res += 1
            # cur_xor = cur_xor ^ cur_xor
            # cur_xor = cur_xor ^ nums[i-(k-1)]
            cur_xor = nums[i-(k-1)]
            i += 1
        return res

    def minChanges(self, nums, k: int) -> int:
        l = len(nums)
        for i range(0, l, k):


nums = [1,2,0,3,0]
k = 1
nums = [3,4,5,2,1,7,3,4,7]
k = 3
nums = [26,19,19,28,13,14,6,25,28,19,0,15,25,11]
k = 3
s = Solution()
print(s.minChanges(nums, k))
