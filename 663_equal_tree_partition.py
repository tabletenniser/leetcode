'''
Given a binary tree with n nodes, your task is to check if it's possible to partition the tree to two trees which have the equal sum of values after removing exactly one edge on the original tree.

Example 1:
Input:
    5
   / \
  10 10
    /  \
   2   3

Output: True
Explanation:
    5
   /
  10

Sum: 15

   10
  /  \
 2    3

Sum: 15
Example 2:
Input:
    1
   / \
  2  10
    /  \
   2   20

Output: False
Explanation: You can't split the tree into two trees with equal sum after removing exactly one edge on the tree.
Note:
The range of tree node value is in the range of [-100000, 100000].
1 <= n <= 10000
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def find_sum(self, node):
        if node == None:
            return 0
        return self.find_sum(node.left) + node.val + self.find_sum(node.right)
    
    def find_target(self, node, target):
        if node == None:
            return False, 0
        if node.left == None and node.right == None:
            return (node.val == target), node.val
        r, s = self.find_target(node.left, target)
        if r == True:
            return r,s
        r2, s2 = self.find_target(node.right, target)
        if r2 == True:
            return r2,s2
        new_sum = s+node.val+s2
        return (new_sum == target), new_sum        
        
    def checkEqualTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root.left == None and root.right == None:
            return False
        tree_sum = self.find_sum(root)
        if tree_sum % 2 == 1:
            return False
        result, _ = self.find_target(root, tree_sum / 2)
        return result
