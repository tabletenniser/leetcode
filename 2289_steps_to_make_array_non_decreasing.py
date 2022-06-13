"""
2289. Steps to Make Array Non-decreasing
You are given a 0-indexed integer array nums. In one step, remove all elements nums[i] where nums[i - 1] > nums[i] for all 0 < i < nums.length.
Return the number of steps performed until nums becomes a non-decreasing array.

Example 1:
Input: nums = [5,3,4,4,7,3,6,11,8,5,11]
Output: 3
Explanation: The following are the steps performed:
- Step 1: [5,3,4,4,7,3,6,11,8,5,11] becomes [5,4,4,7,6,11,11]
- Step 2: [5,4,4,7,6,11,11] becomes [5,4,7,11,11]
- Step 3: [5,4,7,11,11] becomes [5,7,11,11]
[5,7,11,11] is a non-decreasing array. Therefore, we return 3.

Example 2:
Input: nums = [4,5,7,7,13]
Output: 0
Explanation: nums is already a non-decreasing array. Therefore, we return 0.
Constraints:
1 <= nums.length <= 105
1 <= nums[i] <= 109
"""
from typing import List
class Solution:
    def totalSteps1(self, nums: List[int]) -> int:
        stack = [(nums[0], 0)]
        res = 0
        for num in nums[1:]:
            max_pct = 0
            while stack and num >= stack[-1][0]:
                _, pct = stack.pop()
                max_pct = max(max_pct, pct)
            max_pct = max_pct + 1 if stack else 0
            res = max(res, max_pct)
            stack.append((num, max_pct))
        return res

    def totalSteps(self, nums: List[int]) -> int:
        stack = []
        L = len(nums)
        res = 0
        for i in range(L-1, -1, -1):
            ct = 0
            while stack and nums[i] > stack[-1][0]:
                # res = max(res, len(stack))
                _, prev_count = stack.pop()
                ct = max(ct+1, prev_count)
            res = max(res, ct)
            stack.append((nums[i], ct))
            # print(nums[i], stack, res)
        # print(res)
        return res


nums = [5,3,4,4,7,3,6,11,8,5,11]
s = Solution()
assert s.totalSteps(nums) == 3
assert s.totalSteps([7,1,2,3,4,5,6]) == 6
assert s.totalSteps([1,2,3,4,5,6]) == 0
assert s.totalSteps([5,3,1,2,4,6]) == 3
assert s.totalSteps([5,3,4,1,2,6]) == 2
