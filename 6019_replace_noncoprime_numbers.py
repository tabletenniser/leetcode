'''
You are given an array of integers nums. Perform the following steps:
Find any two adjacent numbers in nums that are non-coprime.
If no such numbers are found, stop the process.
Otherwise, delete the two numbers and replace them with their LCM (Least Common Multiple).
Repeat this process as long as you keep finding two adjacent non-coprime numbers.
Return the final modified array. It can be shown that replacing adjacent non-coprime numbers in any arbitrary order will lead to the same result.
The test cases are generated such that the values in the final array are less than or equal to 108.
Two values x and y are non-coprime if GCD(x, y) > 1 where GCD(x, y) is the Greatest Common Divisor of x and y.

Example 1:
Input: nums = [6,4,3,2,7,6,2]
Output: [12,7,6]
Explanation: 
- (6, 4) are non-coprime with LCM(6, 4) = 12. Now, nums = [12,3,2,7,6,2].
- (12, 3) are non-coprime with LCM(12, 3) = 12. Now, nums = [12,2,7,6,2].
- (12, 2) are non-coprime with LCM(12, 2) = 12. Now, nums = [12,7,6,2].
- (6, 2) are non-coprime with LCM(6, 2) = 6. Now, nums = [12,7,6].
There are no more adjacent non-coprime numbers in nums.
Thus, the final modified array is [12,7,6].
Note that there are other ways to obtain the same resultant array.

Example 2:
Input: nums = [2,2,1,1,3,3,3]
Output: [2,1,1,3]
Explanation: 
- (3, 3) are non-coprime with LCM(3, 3) = 3. Now, nums = [2,2,1,1,3,3].
- (3, 3) are non-coprime with LCM(3, 3) = 3. Now, nums = [2,2,1,1,3].
- (2, 2) are non-coprime with LCM(2, 2) = 2. Now, nums = [2,1,1,3].
There are no more adjacent non-coprime numbers in nums.
Thus, the final modified array is [2,1,1,3].
Note that there are other ways to obtain the same resultant array.

Constraints:
1 <= nums.length <= 105
1 <= nums[i] <= 105
The test cases are generated such that the values in the final array are less than or equal to 108.
'''
import math
class Solution:
    def replaceNonCoprimes(self, input_nums):
        def rec(nums):
            if len(nums) == 1:
                return nums
            res = []
            i = 0
            while i < len(nums) - 1:
                a, b = nums[i], nums[i+1]
                # print(i, a, b)
                gcd = math.gcd(a,b)
                while i < len(nums) - 1 and gcd > 1:
                    a, b = math.lcm(a,b), nums[i+1]
                    gcd = math.gcd(a,b)
                    if gcd == 1:
                        break
                    i += 1
                if gcd > 1:
                    res.append(math.lcm(a,b))
                else:
                    res.append(a)
                    if i+1 >= len(nums) - 1:
                        res.append(b)
                i += 1
            return res
        while True:
            L_b = len(input_nums)
            # print(input_nums, L_b)
            input_nums = rec(input_nums)
            if len(input_nums) == L_b:
                return input_nums
        return None

s = Solution()
nums = [9999,10001,1] * 10000
res = s.replaceNonCoprimes(nums)
print(res)
