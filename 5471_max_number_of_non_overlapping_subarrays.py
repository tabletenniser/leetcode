'''
Given an array nums and an integer target.
Return the maximum number of non-empty non-overlapping subarrays such that the sum of values in each subarray is equal to target.


Example 1:
Input: nums = [1,1,1,1,1], target = 2
Output: 2
Explanation: There are 2 non-overlapping subarrays [1,1,1,1,1] with sum equals to target(2).

Example 2:
Input: nums = [-1,3,5,1,4,2,-9], target = 6
Output: 2
Explanation: There are 3 subarrays with sum equal to 6.
([5,1], [4,2], [3,5,1,4,2,-9]) but only the first 2 are non-overlapping.

Example 3:
Input: nums = [-2,6,6,3,5,4,1,2,8], target = 10
Output: 3

Example 4:
Input: nums = [0,0,0], target = 0
Output: 3

Constraints:
1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
0 <= target <= 10^6
'''
class Solution:
    def maxNonOverlapping(self, nums, target):
        i = 0
        cur_sum = 0
        ht = {0: [-1]}
        sub_sum = [None for _ in range(len(nums)+1)]
        sub_sum[0] = 0
        while i < len(nums):
            cur_sum += nums[i]
            val = ht.get(cur_sum, [])
            val.append(i)
            ht[cur_sum] = val
            sub_sum[i+1] = cur_sum
            i += 1
        prev_i = -1
        res = 0
        for i,n in enumerate(nums):
            key = sub_sum[i+1] - target
            if key in ht:
                # print(i, sub_sum[i+1],key,ht[key],prev_i,i)
                for index in ht[key]:
                    if index >= prev_i and index < i:
                        res += 1
                        prev_i = i
                        break
        # print(ht,sub_sum)
        return res

nums = [-1,3,5,1,4,2,-9]
target = 6
nums = [1,1,1,1,1]
target = 2
nums = [-2,6,6,3,5,4,1,2,8]
target = 10
# nums = [0,0,0]
# target = 0
s = Solution()
print(s.maxNonOverlapping(nums, target))
