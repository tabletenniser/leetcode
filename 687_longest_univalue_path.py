'''
Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.

Note: The length of path between two nodes is represented by the number of edges between them.

Example 1:

Input:

              5
             / \
            4   5
           / \   \
          1   1   5
Output:

2
Example 2:

Input:

              1
             / \
            4   5
           / \   \
          4   4   5
Output:

2
Note: The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lup_rec(self, root, val):
        if root == None or root.val != val:
            return 0, 0
        if root.left == None and root.right == None:
            return 1, 1
        parent_value = max(self.lup_rec(root.left, val),
            self.lup_rec(root.right, val)) + 1

        l, max_l = self.lup_rec(root.left, val)
        r, max_r = self.lup_rec(root.right, val)
        return max(l, r) + 1, max(l + r + 1, max_l, max_r)

    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        _, res = self.lup_rec(root, root.val)
