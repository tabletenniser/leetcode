'''
Given the string croakOfFrogs, which represents a combination of the string "croak" from different frogs, that is, multiple frogs can croak at the same time, so multiple “croak” are mixed. Return the minimum number of different frogs to finish all the croak in the given string.

A valid "croak" means a frog is printing 5 letters ‘c’, ’r’, ’o’, ’a’, ’k’ sequentially. The frogs have to print all five letters to finish a croak. If the given string is not a combination of valid "croak" return -1.

Example 1:
Input: croakOfFrogs = "croakcroak"
Output: 1
Explanation: One frog yelling "croak" twice.

Example 2:
Input: croakOfFrogs = "crcoakroak"
Output: 2
Explanation: The minimum number of frogs is two.
The first frog could yell "crcoakroak".
The second frog could yell later "crcoakroak".

Example 3:
Input: croakOfFrogs = "croakcrook"
Output: -1
Explanation: The given string is an invalid combination of "croak" from different frogs.

Example 4:
Input: croakOfFrogs = "croakcroa"
Output: -1

Constraints:

1 <= croakOfFrogs.length <= 10^5
All characters in the string are: 'c', 'r', 'o', 'a' or 'k'.
'''
# from collections import defaultdict
class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        ht = {'c': 0, 'r': 0, 'o': 0, 'a': 0, 'k': 0}
        res = 0
        for ch in croakOfFrogs:
            ht[ch] += 1
            finished_croaks = min(ht.values())
            res = max(res, ht[ch] - finished_croaks)
            # print(ht, finished_croaks)
            if not (ht['c'] >= ht['r'] >= ht['o'] >= ht['a'] >= ht['k']):
                return -1
        prev_v = None
        for v in ht.values():
            if v != prev_v and prev_v is not None:
                return -1
            prev_v = v
        return res

s = Solution()
croakOfFrogs = "oakcr"
# croakOfFrogs = "crcoakroak"
# croakOfFrogs = "croakcrook"
res = s.minNumberOfFrogs(croakOfFrogs)
print(res)
