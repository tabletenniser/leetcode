'''
Given two strings s and t, you want to transform string s into string t using the following operation any number of times:
Choose a non-empty substring in s and sort it in-place so the characters are in ascending order.
For example, applying the operation on the underlined substring in "14234" results in "12344".
Return true if it is possible to transform string s into string t. Otherwise, return false.
A substring is a contiguous sequence of characters within a string.

Example 1:
Input: s = "84532", t = "34852"
Output: true
Explanation: You can transform s into t using the following sort operations:
"84532" (from index 2 to 3) -> "84352"
"84352" (from index 0 to 2) -> "34852"
Example 2:
Input: s = "34521", t = "23415"
Output: true
Explanation: You can transform s into t using the following sort operations:
"34521" -> "23451"
"23451" -> "23415"
Example 3:
Input: s = "12345", t = "12435"
Output: false
Example 4:
Input: s = "1", t = "2"
Output: false

Constraints:
s.length == t.length
1 <= s.length <= 105
s and t only contain digits from '0' to '9'.
'''
class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        s_arr = list(s)
        sorted_s = sorted(s_arr)
        t_arr = list(t)
        sorted_t = sorted(t_arr)
        if sorted_s != sorted_t:
            return False
        i = 0
        while i < len(s_arr):
            if s_arr[i] == t_arr[i]:
                i += 1
                continue
            if s_arr[i] < t_arr[i]:
                return False
            j = i + 1
            while True:
                if s_arr[j] == t_arr[i]:
                    break
                j += 1
            for k in range(j, i, -1):
                s_arr[k] = s_arr[k-1]
            s_arr[i] = t_arr[i]
            print(s_arr, t_arr, i, j)
            i += 1
        return True

s = "84532"
t = "34852"
sol = Solution()
print(sol.isTransformable(s, t))
