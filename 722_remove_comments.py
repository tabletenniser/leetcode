'''
Given a C++ program, remove comments from it. The program source is an array where source[i] is the i-th line of the source code. This represents the result of splitting the original source code string by the newline character \n.

In C++, there are two types of comments, line comments, and block comments.

The string // denotes a line comment, which represents that it and rest of the characters to the right of it in the same line should be ignored.

The string /* denotes a block comment, which represents that all characters until the next (non-overlapping) occurrence of */ should be ignored. (Here, occurrences happen in reading order: line by line from left to right.) To be clear, the string /*/ does not yet end the block comment, as the ending would be overlapping the beginning.

The first effective comment takes precedence over others: if the string // occurs in a block comment, it is ignored. Similarly, if the string /* occurs in a line or block comment, it is also ignored.

If a certain line of code is empty after removing comments, you must not output that line: each string in the answer list will be non-empty.

There will be no control characters, single quote, or double quote characters. For example, source = "string s = "/* Not a comment. */";" will not be a test case. (Also, nothing else such as defines or macros will interfere with the comments.)

It is guaranteed that every open block comment will eventually be closed, so /* outside of a line or block comment always starts a new comment.

Finally, implicit newline characters can be deleted by block comments. Please see the examples below for details.

After removing the comments from the source code, return the source code in the same format.

Example 1:
Input: 
source = ["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]

The line by line code is visualized as below:
/*Test program */
int main()
{ 
  // variable declaration 
int a, b, c;
/* This is a test
   multiline  
   comment for 
   testing */
a = b + c;
}

Output: ["int main()","{ ","  ","int a, b, c;","a = b + c;","}"]

The line by line code is visualized as below:
int main()
{ 
  
int a, b, c;
a = b + c;
}

Explanation: 
The string /* denotes a block comment, including line 1 and lines 6-9. The string // denotes line 4 as comments.
Example 2:
Input: 
source = ["a/*comment", "line", "more_comment*/b"]
Output: ["ab"]
Explanation: The original source string is "a/*comment\nline\nmore_comment*/b", where we have bolded the newline characters.  After deletion, the implicit newline characters are deleted, leaving the string "ab", which when delimited by newline characters becomes ["ab"].
Note:

The length of source is in the range [1, 100].
The length of source[i] is in the range [0, 80].
Every open block comment is eventually closed.
There are no single-quote, double-quote, or control characters in the source code.
'''
class Solution(object):
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        # input_str = '\n'.join(source)
        # print input_str
        result = []
        cur_line_is_commented = False
        for line in source:
            combine_to_line_above = False
            string_to_be_processed = line[:]

            if cur_line_is_commented:
                block_comment_end = string_to_be_processed.find('*/')
                if block_comment_end != -1:
                    string_to_be_processed = string_to_be_processed[block_comment_end+2:]
                    cur_line_is_commented = False
                    combine_to_line_above = True
                else:
                    continue

            line_comment_index = string_to_be_processed.find('//')
            block_comment_start = string_to_be_processed.find('/*')
            if line_comment_index != -1 and \
                    (block_comment_start == -1 or line_comment_index < block_comment_start):
                if line_comment_index != 0:
                    if combine_to_line_above:
                        result[-1] += string_to_be_processed[:line_comment_index]
                    else:
                        result.append(string_to_be_processed[:line_comment_index])
                continue

            block_comment_end = None
            assert not cur_line_is_commented
            result_line = ''
            while block_comment_start >= 0:
                result_line += string_to_be_processed[:block_comment_start]
                cur_line_is_commented = True

                string_to_be_processed = string_to_be_processed[block_comment_start+2:]
                block_comment_end = string_to_be_processed.find('*/')
                if block_comment_end == -1:
                    break

                cur_line_is_commented = False
                string_to_be_processed = string_to_be_processed[block_comment_end+2:]
                # print string_to_be_processed
                line_comment_index = string_to_be_processed.find('//')
                block_comment_start = string_to_be_processed.find('/*')
                if line_comment_index != -1 and \
                        (block_comment_start == -1 or line_comment_index < block_comment_start):
                    string_to_be_processed = string_to_be_processed[:line_comment_index]
                    break


            if not cur_line_is_commented:
                result_line += string_to_be_processed
            if len(result_line) > 0:
                if combine_to_line_above:
                    result[-1] += result_line
                else:
                    result.append(result_line)
        return result


s = Solution()
print s.removeComments(["/*/dadb/*/aec*////*//*ee*//*//b*////*badbda//*bbacdbbd*//ceb//*cdd//**//de*////*","ec//*//*eebd/*/*//*////*ea/*/bc*//cbdacbeadcac/*/cee*//bcdcdde*//adabeaccdd//*", 'blank'])
print s.removeComments(["a/*/b//*c","blank","d/*/e*//f"])
print s.removeComments(["a//*b//*c","blank","d/*/e*//f"])
print s.removeComments(["struct Node{", "    /*/ declare members;/**/", "    int size;", "    /**/int val;", "};"])
print s.removeComments(["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"])
print s.removeComments(["a/*comment", "line", "more_comment*/b"])
