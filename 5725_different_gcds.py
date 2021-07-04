'''
You are given an array nums that consists of positive integers.
The GCD of a sequence of numbers is defined as the greatest integer that divides all the numbers in the sequence evenly.
For example, the GCD of the sequence [4,6,16] is 2.
A subsequence of an array is a sequence that can be formed by removing some elements (possibly none) of the array.
For example, [2,5,10] is a subsequence of [1,2,1,2,4,1,5,10].
Return the number of different GCDs among all non-empty subsequences of nums.

Example 1:
Input: nums = [6,10,3]
Output: 5
Explanation: The figure shows all the non-empty subsequences and their GCDs.
The different GCDs are 6, 10, 3, 2, and 1.
Example 2:
Input: nums = [5,15,40,5,6]
Output: 7
Constraints:
1 <= nums.length <= 105
1 <= nums[i] <= 2 * 105
'''
class TrieNode:
    def __init__(self):
        self.hasValue = False
        self.children = dict{}

class Solution:
    def generatePrimes(self):
        primes = [2,3,5]
        for i in range(7, 1000):
            isPrimes = True
            for p in primes:
                if i % p == 0:
                    isPrimes = False
                    break
            if isPrimes:
                primes.append(i)
        return primes
    def factor(self,num):
        i = 0
        res = []
        while num > 1 and i < len(self.primes) and self.primes[i] * self.primes[i] <= num:
            if num % self.primes[i] == 0:
                num = num // self.primes[i]
                res.append(self.primes[i])
            else:
                i += 1
        if num > 0:
            res.append(num)
        return res
    def countDifferentSubsequenceGCDs(self, nums) -> int:
        self.primes = self.generatePrimes()
        # print(primes)
        root = TrieNode()
        for n in nums:
            factors = self.factor(n)
            print(n, factors)
            cur = root
            for f in factors:
                if f in cur.children:
                    cur = cur.children[f]
                else:
                    newNode = TrieNode()
                    cur.children[f] = newNode
                    cur = cur.children[f]
            cur.hasValue = True

s = Solution()
nums = [5,15,40,5,6]
print(s.countDifferentSubsequenceGCDs(nums))
