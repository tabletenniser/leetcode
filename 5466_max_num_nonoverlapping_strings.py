'''
Given a string s of lowercase letters, you need to find the maximum number of non-empty substrings of s that meet the following conditions:
The substrings do not overlap, that is for any two substrings s[i..j] and s[k..l], either j < k or i > l is true.
A substring that contains a certain character c must also contain all occurrences of c.
Find the maximum number of substrings that meet the above conditions. If there are multiple solutions with the same number of substrings, return the one with minimum total length. It can be shown that there exists a unique solution of minimum total length.

Notice that you can return the substrings in any order.
Example 1:
Input: s = "adefaddaccc"
Output: ["e","f","ccc"]
Explanation: The following are all the possible substrings that meet the conditions:
[
  "adefaddaccc"
  "adefadda",
  "ef",
  "e",
  "f",
  "ccc",
]
If we choose the first string, we cannot choose anything else and we'd get only 1. If we choose "adefadda", we are left with "ccc" which is the only one that doesn't overlap, thus obtaining 2 substrings. Notice also, that it's not optimal to choose "ef" since it can be split into two. Therefore, the optimal way is to choose ["e","f","ccc"] which gives us 3 substrings. No other solution of the same number of substrings exist.

Example 2:
Input: s = "abbaccd"
Output: ["d","bb","cc"]
Explanation: Notice that while the set of substrings ["d","abba","cc"] also has length 3, it's considered incorrect since it has larger total length.

Constraints:
1 <= s.length <= 10^5
s contains only lowercase English letters.
'''
class Solution:
    def overlap(self, existing_segments, start, end):
        for seg in existing_segments:
            if not (start > seg[1] or end < seg[0]):
                return True
        return False

    def maxNumOfSubstrings(self, s: str):
        start_ht = dict()
        end_ht = dict()
        for i, ch in enumerate(s):
            end_ht[ch] = i
            if ch not in start_ht:
                start_ht[ch] = i
        expanded_ht = dict()
        diff_ht = dict()
        for key, start in start_ht.items():
            end = end_ht[key]
            new_s, new_e = start, end
            for k in range(start, end + 1):
                if start_ht[s[k]] < new_s:
                    new_s = start_ht[s[k]]
                if end_ht[s[k]] > new_e:
                    new_e = end_ht[s[k]]
            expanded_ht[key] = (new_s, new_e)
            diff_ht[key] = new_e - new_s
        sorted_diff_ht = {k: v for k, v in sorted(diff_ht.items(), key=lambda item: item[1])}
        print(sorted_diff_ht)
        print(expanded_ht)
        res = []
        existing_segments = []
        for k, v in sorted_diff_ht.items():
            start, end = expanded_ht[k]
            if not self.overlap(existing_segments, start, end):
                existing_segments.append((start, end))
                res.append(s[start: end+1])
            print(existing_segments)
        return res

s = "adefaddaccc"
# s = "abbaccd"
# s = "abab"
s= "cabcccbaa"
sol = Solution()
print(sol.maxNumOfSubstrings(s))
