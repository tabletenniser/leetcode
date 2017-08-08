'''
Given a binary tree, return all duplicate subtrees. For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with same node values.

Example 1:
        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4
The following are two duplicate subtrees:
      2
     /
    4
and
    4
Therefore, you need to return above trees' root in the form of a list.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def fdsRecursive(self, node, hash_map, result):
        if node == None:
            return ''
        serialize_string = '('+self.fdsRecursive(node.left, hash_map, result)+str(node.val)+self.fdsRecursive(node.right, hash_map, result)
        if serialize_string in hash_map:
            if hash_map[serialize_string] == 1:
                result.append(node)
            hash_map[serialize_string] += 1
        else:
            hash_map[serialize_string] = 1
        return serialize_string

    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        result = []
        hash_map = dict()
        self.fdsRecursive(root, hash_map, result)
        return result
