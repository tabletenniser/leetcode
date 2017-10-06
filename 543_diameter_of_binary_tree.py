'''
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \
      4   5
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dbt_rec(node):
            if node == None:
                return 0, 0
            l, l_res = dbt_rec(node.left)
            r, r_res = dbt_rec(node.right)
            res = max(l_res, r_res, l + r + 1)
            return max(l, r) + 1, res
        _, res = dbt_rec(root)
        return res - 1
