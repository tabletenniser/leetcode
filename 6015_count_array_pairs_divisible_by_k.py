'''
Given a 0-indexed integer array nums of length n and an integer k, return the number of pairs (i, j) such that:
0 <= i < j <= n - 1 and
nums[i] * nums[j] is divisible by k.

Example 1:
Input: nums = [1,2,3,4,5], k = 2
Output: 7
Explanation: 
The 7 pairs of indices whose corresponding products are divisible by 2 are
(0, 1), (0, 3), (1, 2), (1, 3), (1, 4), (2, 3), and (3, 4).
Their products are 2, 4, 6, 8, 10, 12, and 20 respectively.
Other pairs such as (0, 2) and (2, 4) have products 3 and 15 respectively, which are not divisible by 2.    

Example 2:
Input: nums = [1,2,3,4], k = 5
Output: 0
Explanation: There does not exist any pair of indices whose corresponding product is divisible by 5.

Constraints:
1 <= nums.length <= 105
1 <= nums[i], k <= 105
'''
import math
class Solution:
    def coutPairs(self, nums, k: int) -> int:
        if k == 1:
            L = len(nums)
            return L * (L-1)//2
        coprime_count = 0
        include_count = 0
        interesting_nums = dict()
        in_count = 0
        for n in nums:
            g = math.gcd(n, k)
            if g == 1:
                coprime_count += 1
            elif g == k:
                include_count += 1
            else:
                interesting_nums[g] = interesting_nums.get(g, 0) + 1
                in_count += 1
        # print(coprime_count, include_count, interesting_nums)
        res = 0
        in_lst = list(interesting_nums.keys())
        for i, key1 in enumerate(in_lst):
            key1 = in_lst[i]
            for j in range(i, len(in_lst)):
                key2 = in_lst[j]
                if (key1 * key2) % k == 0:
                    if key1 == key2:
                        res += interesting_nums[key1] * (interesting_nums[key1]-1) // 2
                    else:
                        res += interesting_nums[key1] * interesting_nums[key2]
        res += include_count * (coprime_count+in_count)
        res += (include_count * (include_count-1)) // 2
        return res

s = Solution()
nums = [5,8]
k = 1
nums = [10,10,6,9,3,7,4,3,8,8]
k = 4
res = s.coutPairs(nums, k)
print(res)
