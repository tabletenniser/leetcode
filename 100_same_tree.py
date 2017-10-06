'''
Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left, right):
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if q == None and p == None:
            return True
        if q == None or p == None or q.val != p.val:
            return False
        return self.isSameTree(q.left, p.left) and self.isSameTree(q.right, p.right)

s = Solution()
n1 = TreeNode(1, None, None)
n2 = TreeNode(1, n1, None)
assert(s.isSameTree(n1, n1))
assert(not s.isSameTree(n2, n1))
