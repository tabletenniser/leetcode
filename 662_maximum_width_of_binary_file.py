'''
Given a binary tree, write a function to get the maximum width of the given tree. The width of a tree is the maximum width among all levels. The binary tree has the same structure as a full binary tree, but some nodes are null.

The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the null nodes between the end-nodes are also counted into the length calculation.

Example 1:
Input: 

           1
         /   \
        3     2
       / \     \  
      5   3     9 

Output: 4
Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
Example 2:
Input: 

          1
         /  
        3    
       / \       
      5   3     

Output: 2
Explanation: The maximum width existing in the third level with the length 2 (5,3).
Example 3:
Input: 

          1
         / \
        3   2 
       /        
      5      

Output: 2
Explanation: The maximum width existing in the second level with the length 2 (3,2).
Example 4:
Input: 

          1
         / \
        3   2
       /     \  
      5       9 
     /         \
    6           7
Output: 8
Explanation:The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).


Note: Answer will in the range of 32-bit signed integer.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # def widthOfBinaryTree(self, root):
    #     if root == None:
    #         return 0
    #     max_width = 1
    #     cur_width = 1
    #     l, r = root, root
    #     while l != None and r != None:
            
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        queue = []
        queue.append(root)
        max_width = 1
        while len(queue) > 0:
            next_level = []
            while len(queue) > 0:
                elem = queue.pop(0)
                if type(elem) == int:
                    next_level.append(elem*2)
                elif elem != None:
                    if elem.left == None and elem.right == None:
                        next_level.append(2)
                    elif elem.left == None:
                        next_level.append(1)
                        next_level.append(elem.right)
                    elif elem.right == None:
                        next_level.append(elem.left)
                        next_level.append(1)
                    else:
                        next_level.append(elem.left)
                        next_level.append(elem.right)
            #Filter None at the beginning and end
            while len(next_level) > 0 and type(next_level[-1]) == int:
                next_level.pop(-1)
            while len(next_level) > 0 and type(next_level[0]) == int:
                next_level.pop(0)
            print next_level
            cur_width = 0
            for e in next_level:
                if type(e) == int:
                    cur_width += e
                else:
                    cur_width += 1
            if cur_width > max_width:
                max_width = cur_width
            queue=next_level
        return max_width
