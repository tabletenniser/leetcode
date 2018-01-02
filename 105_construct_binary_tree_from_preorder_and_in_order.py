'''
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        assert len(preorder) == len(inorder)
        if len(inorder) == 0:
            return None
        if len(inorder) == 1:
            return TreeNode(inorder[0])
        val = preorder[0]
        node = TreeNode(val)
        size_of_left_tree = inorder.index(val)
        left_n = self.buildTree(preorder[1:size_of_left_tree+1],
            inorder[:size_of_left_tree])
        right_n = self.buildTree(preorder[size_of_left_tree+1:],
            inorder[size_of_left_tree+1:])
        node.left = left_n
        node.right = right_n
        return node

s = Solution()
print s.buildTree([1,4,2,3,5], [1,2,3,4,5])
