'''
5631. Jump Game VI
User Accepted:0
User Tried:0
Total Accepted:0
Total Submissions:0
Difficulty:Medium
You are given a 0-indexed integer array nums and an integer k.

You are initially standing at index 0. In one move, you can jump at most k steps forward without going outside the boundaries of the array. That is, you can jump from index i to any index in the range [i + 1, min(n - 1, i + k)] inclusive.

You want to reach the last index of the array (index n - 1). Your score is the sum of all nums[j] for each index j you visited in the array.

Return the maximum score you can get.



Example 1:

Input: nums = [1,-1,-2,4,-7,3], k = 2
Output: 7
Explanation: You can choose your jumps forming the subsequence [1,-1,4,3] (underlined above). The sum is 7.
Example 2:

Input: nums = [10,-5,-2,4,0,3], k = 3
Output: 17
Explanation: You can choose your jumps forming the subsequence [10,4,3] (underlined above). The sum is 17.
Example 3:

Input: nums = [1,-5,-20,4,-1,3,-6,-3], k = 2
Output: 0


Constraints:

 1 <= nums.length, k <= 105
-104 <= nums[i] <= 104
'''
class Solution:
    def maxResult(self, nums, k):
        index = len(nums) - 2
        ht = [-9999999999 for _ in range(len(nums))]
        ht[-1] = nums[-1]
        dequeue = [(ht[-1], len(nums) -1)]
        while index >= 0:
            if dequeue[0][1] > index + k:
                del dequeue[0]
            j = dequeue[0][1]
            ht[index] = ht[j] + nums[index]
            while len(dequeue) > 0 and ht[index] > dequeue[-1][0]:
                del dequeue[-1]
            dequeue.append((ht[index], index))
            index -= 1
        # print(ht)
        return ht[0]

s = Solution()
nums=[1,-1,-2,4,-7,3]
k=2
# nums=[10,-5,-2,4,0,3]
# k=3
# nums = [1,-5,-20,4,-1,3,-6,-3]
# k = 2
# k = 99000
# nums = [9999, -9999]*40000
print(s.maxResult(nums,k))