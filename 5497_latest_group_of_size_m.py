'''
Given an array arr that represents a permutation of numbers from 1 to n. You have a binary string of size n that initially has all its bits set to zero.
At each step i (assuming both the binary string and arr are 1-indexed) from 1 to n, the bit at position arr[i] is set to 1. You are given an integer m and you need to find the latest step at which there exists a group of ones of length m. A group of ones is a contiguous substring of 1s such that it cannot be extended in either direction.
Return the latest step at which there exists a group of ones of length exactly m. If no such group exists, return -1.

Example 1:
Input: arr = [3,5,1,2,4], m = 1
Output: 4
Explanation:
Step 1: "00100", groups: ["1"]
Step 2: "00101", groups: ["1", "1"]
Step 3: "10101", groups: ["1", "1", "1"]
Step 4: "11101", groups: ["111", "1"]
Step 5: "11111", groups: ["11111"]
The latest step at which there exists a group of size 1 is step 4.
Example 2:
Input: arr = [3,1,5,4,2], m = 2
Output: -1
Explanation:
Step 1: "00100", groups: ["1"]
Step 2: "10100", groups: ["1", "1"]
Step 3: "10101", groups: ["1", "1", "1"]
Step 4: "10111", groups: ["1", "111"]
Step 5: "11111", groups: ["11111"]
No group of size 2 exists during any step.
Example 3:
Input: arr = [1], m = 1
Output: 1
Example 4:
Input: arr = [2,1], m = 2
Output: 2

Constraints:
n == arr.length
1 <= n <= 10^5
1 <= arr[i] <= n
All integers in arr are distinct.
1 <= m <= arr.length
'''
from bisect import bisect_left
class Solution:
    def findLatestStep(self, arr, m: int) -> int:
        n = len(arr)
        segments = [(1, n)]
        if m == n:
            return n
        for cur_iter, zero in enumerate(arr[::-1]):
            index = bisect_left(segments, (zero, 9999999999)) - 1
            print(segments, zero, index)
            seg = segments[index]
            if seg[1] == 1 and seg[0] == zero:
                del segments[index]
            elif seg[1] == 1:
                assert False
            else:
                del segments[index]
                first_length = zero-seg[0]
                second_length = seg[0]+seg[1]-1-zero
                if first_length == m or second_length == m:
                    return n - cur_iter - 1
                if second_length >= 1:
                    segments.insert(index, (zero+1, second_length))
                if first_length >= 1:
                    segments.insert(index, (seg[0], first_length))
            # print(segments)
        return -1


# arr = [3,5,1,2,4]
arr = [3,1,5,4,2]
m = 1
# arr = [4,3,2,1]
# m = 1
# arr = [2,1]
# m = 2
# arr = [1]
# m = 1
s = Solution()
print(s.findLatestStep(arr, m))
