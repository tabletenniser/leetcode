'''
Given two sentences words1, words2 (each represented as an array of strings), and a list of similar word pairs pairs, determine if two sentences are similar.

For example, "great acting skills" and "fine drama talent" are similar, if the similar word pairs are pairs = [["great", "fine"], ["acting","drama"], ["skills","talent"]].

Note that the similarity relation is not transitive. For example, if "great" and "fine" are similar, and "fine" and "good" are similar, "great" and "good" are not necessarily similar.

Also, a word is always similar with itself. For example, the sentences words1 = ["great"], words2 = ["great"], pairs = [] are similar, even though there are no specified similar word pairs.

Note:

The length of words1 and words2 will not exceed 1000.
The length of pairs will not exceed 2000.
The length of each pairs[i] will be 2.
The length of each words[i] and pairs[i][j] will be in the range [1, 20].
'''
class Solution(object):
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2):
            return False
        d = dict()
        for p in pairs:
            if p[0] not in d:
                d[p[0]] = set()
            d[p[0]].add(p[1])
            if p[1] not in d:
                d[p[1]] = set()
            d[p[1]].add(p[0])

        for i in xrange(len(words1)):
            w1, w2 = words1[i], words2[i]
            if w1 != w2 and (w1 not in d or w2 not in d[w1]):
                return False
        return True

s = Solution()
pairs = [["great", "fine"], ["acting","drama"], ["skills","talent"]]
assert s.areSentencesSimilar(['great', 'acting', 'skills'], ['fine', 'drama', 'talent'], []) == False
assert s.areSentencesSimilar(['great', 'acting', 'skills'], ['fine', 'drama', 'talent'], pairs)
assert s.areSentencesSimilar(['great', 'acting', 'skills'], ['great', 'acting', 'skills'], [])
