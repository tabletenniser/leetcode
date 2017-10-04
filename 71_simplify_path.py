'''
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
click to show corner cases.
'''
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        folders = path.split('/')
        simplified_folders = []
        for f in folders:
            if f == "." or f == "":
                continue
            elif f == "..":
                if len(simplified_folders) > 0:
                    del simplified_folders[-1]
            else:
                simplified_folders.append(f)
        return "/"+"/".join(simplified_folders) if len(simplified_folders) > 0 else '/'

s = Solution()
assert(s.simplifyPath("/home/") == "/home")
assert(s.simplifyPath("/a/./b/../../c/") == "/c")
assert(s.simplifyPath("/") == "/")
assert(s.simplifyPath("/../") == "/")
assert(s.simplifyPath("///") == "/")
