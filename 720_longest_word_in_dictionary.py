'''
Given a list of strings words representing an English Dictionary, find the longest word in words that can be built one character at a time by other words in words. If there is more than one possible answer, return the longest word with the smallest lexicographical order.

If there is no answer, return the empty string.
Example 1:
Input: 
words = ["w","wo","wor","worl", "world"]
Output: "world"
Explanation: 
The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
Example 2:
Input: 
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
Output: "apple"
Explanation: 
Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".
Note:

All the strings in the input will only contain lowercase letters.
The length of words will be in the range [1, 1000].
The length of words[i] will be in the range [1, 30].
'''
class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        words.sort()
        w_dict = set()
        result = ''
        for w in words:
            w_dict.add(w)

        for w in words:
            can_be_built = True
            for i in xrange(1, len(w)):
                if w[:i] not in w_dict:
                    can_be_built = False
                    break
            if can_be_built and len(w) > len(result):
                result = w
        return result


s = Solution()
print s.longestWord(["w","wo","wor","worl", "world"])
print s.longestWord(["a", "banana", "app", "appl", "ap", "apply", "apple"])
