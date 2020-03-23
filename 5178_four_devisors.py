'''
Given an integer array nums, return the sum of divisors of the integers in that array that have exactly four divisors.

If there is no such integer in the array, return 0.

Example 1:

Input: nums = [21,4,7]
Output: 32
Explanation:
21 has 4 divisors: 1, 3, 7, 21
4 has 3 divisors: 1, 2, 4
7 has 2 divisors: 1, 7
The answer is the sum of divisors of 21 only.

1 <= nums.length <= 10^4
1 <= nums[i] <= 10^5

'''
class Solution:
    def getDivisors(self, n):
        divisors = {1, n}
        upper_bound = int(n ** 0.5) + 1
        for d in range(2, upper_bound):
            if n % d == 0:
                divisors.add(int(d))
                divisors.add(int(n / d))
                if len(divisors) > 4:
                    return 0
        if len(divisors) == 4:
            return sum(divisors)
        return 0

    def sumFourDivisors(self, nums):
        res = 0
        for n in nums:
            res += self.getDivisors(n)
        return res

s = Solution()
nums = [21, 4, 7]
res = s.sumFourDivisors(nums)
print(res)

