"""
Given a string s and a list of strings dict, you need to add a closed pair of bold tag <b> and </b> to wrap the substrings in s that exist in dict. If two such substrings overlap, you need to wrap them together by only one pair of closed bold tag. Also, if two substrings wrapped by bold tags are consecutive, you need to combine them.

Example 1:
    Input: 
        s = "abcxyz123"
        dict = ["abc","123"]
        Output:
        "<b>abc</b>xyz<b>123</b>"
        Example 2:
        Input: 
        s = "aaabbcc"
        dict = ["aaa","aab","bc"]
        Output:
        "<b>aaabbc</b>c"
        Note:
        The given dict won't contain duplicates, and its length won't exceed 100.
        All the strings in input have length in range [1, 1000].
"""
class Solution(object):
    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        import time
        print time.time()
        #dict_set = set(dict)
        
        # Build a trie on dict
        root = {}
        for w in dict:
            cur_dict = root
            for l in w:
                if l not in cur_dict:
                    cur_dict[l] = {}
                cur_dict = cur_dict[l]
            cur_dict['_END'] = '_END'
        #print root
        
        tags = []
        i = 0
        while i < len(s):
            j = i
            end = j
            cur_dict = root
            while j < len(s):
                if s[j] not in cur_dict:
                    break
                cur_dict = cur_dict[s[j]]
                if '_END' in cur_dict:
                    end = j + 1
                j += 1
                
            if end > i and (len(tags) == 0 or end > tags[-1][1]):
                start = i
                if len(tags) > 0 and i <= tags[-1][1]:
                    start = tags[-1][0]
                    del tags[-1]
                tags.append((start, end))
                #print tags
            i += 1
        
        
        print time.time()
        
        s_list = list(s)
        for t in tags[::-1]:
            s_list.insert(t[1], '>')
            s_list.insert(t[1], 'b')
            s_list.insert(t[1], '/')
            s_list.insert(t[1], '<')
            s_list.insert(t[0], '>')
            s_list.insert(t[0], 'b')
            s_list.insert(t[0], '<')
        
        
        #print time.time()
        return ''.join(s_list)
