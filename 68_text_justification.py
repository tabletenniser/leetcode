'''
Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

For example,
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.

Return the formatted lines as:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Note: Each word is guaranteed not to exceed L in length.
'''
class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        if len(words) == 0:
            return []
        i = 0
        cur_len = 0
        cur_words = []
        res = []
        while i < len(words):
            print cur_words, cur_len
            num_spaces = maxWidth - cur_len
            # If words[i] plus a space is longer than available spaces, add cur_words to a new line in res
            if num_spaces - (len(cur_words) - 1) < len(words[i]) + 1:
                line = ''
                if len(cur_words) == 1:
                    line = cur_words[0].ljust(maxWidth)
                else:
                    space_between_words, num_extra_spaces = divmod(num_spaces, len(cur_words)-1)
                    for j in xrange(num_extra_spaces):
                        cur_words[j] += ' '
                    line = (' '*space_between_words).join(cur_words)
                print line, maxWidth
                assert(len(line) == maxWidth)
                res.append(line)
                cur_len = 0
                cur_words = []
            cur_len += len(words[i])
            cur_words.append(words[i])
            i += 1

        res.append(' '.join(cur_words).ljust(maxWidth))
        return res


s = Solution()
print s.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16)
print s.fullJustify(["a", "b", "c"], 1)
print s.fullJustify(["Listen","to","many,","speak","to","a","few."], 6)
