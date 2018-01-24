'''
Given a set of keywords words and a string S, make all appearances of all keywords in S bold. Any letters between <b> and </b> tags become bold.

The returned string should use the least number of tags possible, and of course the tags should form a valid combination.

For example, given that words = ["ab", "bc"] and S = "aabcd", we should return "a<b>abc</b>d". Note that returning "a<b>a<b>b</b>c</b>d" would use more tags, so it is incorrect.

Note:

words has length in range [0, 50].
words[i] has length in range [1, 10].
S has length in range [0, 500].
All characters in words[i] and S are lowercase letters.
'''
class Solution(object):
    def boldWords(self, words, S):
        """
        :type words: List[str]
        :type S: str
        :rtype: str
        """
        def substring_indexes(substring, string):
            """ 
            Generate indices of where substring begins in string

            >>> list(find_substring('me', "The cat says meow, meow"))
            [13, 19]
            """
            last_found = -1  # Begin at -1 so the next position to search from is 0
            while True:
                # Find next index of substring, by starting after its last known position
                last_found = string.find(substring, last_found + 1)
                if last_found == -1:  
                    break  # All occurrences have been found
                yield last_found

        is_bold = [False for _ in xrange(len(S))]
        for w in words:
            indices = list(substring_indexes(w, S))
            for i in indices:
                for j in xrange(i, i+len(w)):
                    is_bold[j] = True
        # print is_bold, S
        result = []
        prev_is_bold = False
        for i in xrange(len(S)):
            if not prev_is_bold and is_bold[i]:
                result.extend(list('<b>'))
                prev_is_bold = True
            elif prev_is_bold and not is_bold[i]:
                result.extend(list('</b>'))
                prev_is_bold = False
            result.append(S[i])

        if prev_is_bold:
            result.extend(list('</b>'))
        return ''.join(result)



s = Solution()
print s.boldWords(['ab', 'bc'], 'aabcd')
print s.boldWords(['ab', 'bc'], 'aabcdababc')
