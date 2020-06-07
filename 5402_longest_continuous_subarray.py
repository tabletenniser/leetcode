'''
Given an array of integers nums and an integer limit, return the size of the longest continuous subarray such that the absolute difference between any two elements is less than or equal to limit.
In case there is no subarray satisfying the given condition return 0.

Example 1:
Input: nums = [8,2,4,7], limit = 4
Output: 2
Explanation: All subarrays are:
[8] with maximum absolute diff |8-8| = 0 <= 4.
[8,2] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
[2] with maximum absolute diff |2-2| = 0 <= 4.
[2,4] with maximum absolute diff |2-4| = 2 <= 4.
[2,4,7] with maximum absolute diff |2-7| = 5 > 4.
[4] with maximum absolute diff |4-4| = 0 <= 4.
[4,7] with maximum absolute diff |4-7| = 3 <= 4.
[7] with maximum absolute diff |7-7| = 0 <= 4.
Therefore, the size of the longest subarray is 2.
Example 2:
Input: nums = [10,1,2,4,7,2], limit = 5
Output: 4
Explanation: The subarray [2,4,7,2] is the longest since the maximum absolute diff is |2-7| = 5 <= 5.
Example 3:
Input: nums = [4,2,2,2,4,4,2,2], limit = 0
Output: 3

Constraints:
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
0 <= limit <= 10^9
'''
from collections import deque
class Solution:
    def longestSubarray(self, nums, limit: int) -> int:
        large_de = deque()
        small_de = deque()
        cur_max = 0
        cur_min = 0
        j = 0
        res = 0
        for i in range(len(nums)):
            n = nums[i]
            # print(j,i,n,small_de,large_de,res)
            while len(small_de) > 0 and n < nums[small_de[-1]]:
                small_de.pop()
            while len(large_de) > 0 and n > nums[large_de[-1]]:
                large_de.pop()
            small_de.append(i)
            large_de.append(i)
            while True:
                # print(small_de, large_de, i, j)
                if nums[large_de[0]] - nums[small_de[0]] <= limit:
                    break
                res = max(res, i - j)
                if large_de[0] < small_de[0]:
                    j = large_de.popleft() + 1
                elif large_de[0] == small_de[0]:
                    j = large_de.popleft() + 1
                    small_de.popleft()
                else:
                    j = small_de.popleft() + 1
                if len(large_de) == 0:
                    large_de.append(i)
                if len(small_de) == 0:
                    small_de.append(i)
                # j = min(small_de[0], large_de[0])
        res = max(res, i + 1 - j)
        return res


s = Solution()
nums = [10,1,2,7,4,8,2]
limit = 6
# nums = [4,2,2,2,4,4,2,2]
# limit = 0
# nums = [8,2,4,7]
# limit = 4
# nums=[7,40,10,10,40,39,96,21,54,73,33,17,2,72,5,76,28,73,59,22,100,91,80,66,5,49,26,45,13,27,74,87,56,76,25,64,14,86,50,38,65,64,3,42,79,52,37,3,21,26,42,73,18,44,55,28,35,87]
# limit=63
nums=[24,12,71,33,5,87,10,11,3,58,2,97,97,36,32,35,15,80,24,45,38,9,22,21,33,68,22,85,35,83,92,38,59,90,42,64,61,15,4,40,50,44,54,25,34,14,33,94,66,27,78,56,3,29,3,51,19,5,93,21,58,91,65,87,55,70,29,81,89,67,58,29,68,84,4,51,87,74,42,85,81,55,8,95,39]
limit = 87
res = s.longestSubarray(nums, limit)
print(res)
