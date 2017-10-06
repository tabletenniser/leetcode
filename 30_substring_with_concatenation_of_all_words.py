'''
You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

For example, given:
s: "barfoothefoobarman"
words: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).
'''
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if len(words) == 0:
            return []
        expects = dict()
        w_len = len(words[0])
        num_of_words = len(words)
        for w in words:
            expects[w] = expects.get(w, 0) + 1

        res = []
        for i in xrange(w_len):
            left, right = i, i
            cur_words = dict()
            cur_count = 0
            while right+w_len <= len(s):
                word = s[right:right+w_len]
                if word in expects:
                    if cur_words.get(word, 0) < expects[word]:
                        cur_words[word] = cur_words.get(word, 0) + 1
                        cur_count += 1
                    else:
                        w = s[left:left+w_len]
                        cur_words[w] = cur_words[w] - 1
                        cur_count -= 1
                        left += w_len
                        right -= w_len
                else:
                    left = right + w_len
                    cur_words = dict()
                    cur_count = 0
                # If valid, add it to res
                if cur_count == num_of_words:
                    res.append(left)
                    w = s[left:left+w_len]
                    cur_words[w] = cur_words[w] - 1
                    cur_count -= 1
                    left += w_len
                right += w_len
        return res

    def findSubstring_2(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if len(words) == 0:
            return []
        expects = dict()
        w_len = len(words[0])
        num_of_words = len(words)
        for w in words:
            expects[w] = expects.get(w, 0) + 1

        res = []
        i = 0
        while i + w_len * num_of_words <= len(s):
            j = 0
            cur_count = dict()
            while j < num_of_words:
                w = s[i + j*w_len : i + (j + 1)*w_len]
                cur_count[w] = cur_count.get(w, 0) + 1
                if w not in expects or cur_count[w] > expects[w]:
                    print expects, cur_count
                    break
                j += 1
            if j == num_of_words:
                res.append(i)
            i += 1
        return res

s = Solution()
print s.findSubstring("barfoothefoobarman", ["foo", "bar"])
print s.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","good"])
