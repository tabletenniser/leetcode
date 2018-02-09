'''
You are given an integer array sorted in ascending order (may contain duplicates), you need to split them into several subsequences, where each subsequences consist of at least 3 consecutive integers. Return whether you can make such a split.

Example 1:
Input: [1,2,3,3,4,5]
Output: True
Explanation:
You can split them into two consecutive subsequences : 
1, 2, 3
3, 4, 5
Example 2:
Input: [1,2,3,3,4,4,5,5]
Output: True
Explanation:
You can split them into two consecutive subsequences : 
1, 2, 3, 4, 5
3, 4, 5
Example 3:
Input: [1,2,3,4,4,5]
Output: False
Note:
The length of the input is in range of [1, 10000]
'''
class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        counts = dict()
        for n in nums:
            counts[n] = counts.get(n, 0) + 1

        tail = dict()
        for n in nums:
            if counts[n] == 0:
                continue
            counts[n] -= 1
            if tail.get(n, 0) > 0:
                tail[n] -= 1
                tail[n+1] = tail.get(n+1, 0) + 1
            elif counts.get(n+1, 0) > 0 and counts.get(n+2, 0) > 0:
                counts[n+1] -= 1
                counts[n+2] -= 1
                tail[n+3] = tail.get(n+3, 0) + 1
            else:
                return False
        return True

s = Solution()
assert s.isPossible([1,2,3,3,4,5])
assert s.isPossible([1,2,3,3,4,4,5,5])
assert s.isPossible([1,2,3,4,4,5]) == False
