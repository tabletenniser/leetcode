'''
We are given N different types of stickers. Each sticker has a lowercase English word on it.

You would like to spell out the given target string by cutting individual letters from your collection of stickers and rearranging them.

You can use each sticker more than once if you want, and you have infinite quantities of each sticker.

What is the minimum number of stickers that you need to spell out the target? If the task is impossible, return -1.

Example 1:

Input:

["with", "example", "science"], "thehat"
Output:

3
Explanation:

We can use 2 "with" stickers, and 1 "example" sticker.
After cutting and rearrange the letters of those stickers, we can form the target "thehat".
Also, this is the minimum number of stickers necessary to form the target string.
Example 2:

Input:

["notice", "possible"], "basicbasic"
Output:

-1
Explanation:

We can't form the target "basicbasic" from cutting letters from the given stickers.
Note:

stickers has length in the range [1, 50].
stickers consists of lowercase English words (without apostrophes).
target has length in the range [1, 15], and consists of lowercase English letters.
In all test cases, all words were chosen randomly from the 1000 most common US English words, and the target was chosen as a concatenation of two random words.
The time limit may be more challenging than usual. It is expected that a 50 sticker test case can be solved within 35ms on average.
'''
import math
class Solution(object):
    def minStickers(self, stickers, target):
        """
        :type stickers: List[str]
        :type target: str
        :rtype: int
        """
        # Create dictionary
        dictionary = [dict() for _ in xrange(26)]
        for s in stickers:
            for ch in s:
                cell = dictionary[ord(ch) - ord('a')]
                cell[s] = cell.get(s, 0) + 1
        # print dictionary

        count = dict()
        for ch in target:
            cell = dictionary[ord(ch) - ord('a')]
            if len(cell) == 0:
                return -1
            count[ch] = count.get(ch, 0) + 1
        # print count

        def dfs(count, chosen_stickers, result):
            # Found a solution
            if len(count) == 0:
                res = 0
                for cs in chosen_stickers.values():
                    res += cs
                return min(result, res)
            ch = count.keys()[0]
            ch_val = count[ch]
            del count[ch]
            cell = dictionary[ord(ch) - ord('a')]
            res = result
            for string in cell.keys():
                old_val = chosen_stickers.get(string, 0)
                new_value = int(math.ceil(ch_val * 1.0 / cell[string]))
                if string not in chosen_stickers or chosen_stickers[string] < new_value:
                    chosen_stickers[string] = new_value
                res = min(res, dfs(count, chosen_stickers, result))
                chosen_stickers[string] = old_val
            count[ch] = ch_val
            return res

        chosen_stickers = dict()
        return dfs(count, chosen_stickers, 99999999)

s = Solution()
# print s.minStickers(["notice", "possible"], "basicbasic")
# print s.minStickers(["with", "example", "science"], "thehat")
# print s.minStickers(["fly","me","charge","mind","bottom"], "centorder")
print s.minStickers(["travel","quotient","nose","wrote","any"], "lastwest")
