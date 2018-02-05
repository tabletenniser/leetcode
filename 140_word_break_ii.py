'''

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. You may assume the dictionary does not contain duplicate words.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].

UPDATE (2017/1/4):
The wordDict parameter had been changed to a list of strings (instead of a set of strings). Please reload the code definition to get the latest changes.

'''
from collections import defaultdict
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        wordDict = set(wordDict)
        hash_table = defaultdict(list)
        for i in xrange(len(s)-1, -1, -1):
            for j in xrange(i+1, len(s)+1):
                if (s[j:] in hash_table or j == len(s)) and s[i:j] in wordDict:
                    if j == len(s):
                        hash_table[s[i:]].append(s[i:j])
                    else:
                        for string in hash_table[s[j:]]:
                            hash_table[s[i:]].append(s[i:j]+' '+string)
        return hash_table[s]

    def wordBreak2(self, s, wordDict):
        wordDict = set(wordDict)
        hash_table = dict()
        def word_break_rec(string):
            if string in hash_table:
                return hash_table[string]
            result = []
            if string in wordDict:
                result.append(string)
            for i in xrange(len(string)):
                if string[:i] in wordDict:
                    words = word_break_rec(string[i:])
                    for w in words:
                        result.append(string[:i]+' '+w)
            hash_table[string] = result
            return result
        return word_break_rec(s)

s = Solution()
string = "aaaaa"
words = ['a', 'aa']
print s.wordBreak(string, words)
print s.wordBreak2(string, words)
assert set(s.wordBreak(string, words)) == set(s.wordBreak2(string, words))

string="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
words=["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
print s.wordBreak(string, words)
