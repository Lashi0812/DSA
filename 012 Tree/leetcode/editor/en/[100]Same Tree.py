# Given the roots of two binary trees p and q, write a function to check if 
# they are the same or not. 
# 
#  Two binary trees are considered the same if they are structurally identical, 
# and the nodes have the same value. 
# 
#  
#  Example 1: 
#  
#  
# Input: p = [1,2,3], q = [1,2,3]
# Output: true
#  
# 
#  Example 2: 
#  
#  
# Input: p = [1,2], q = [1,null,2]
# Output: false
#  
# 
#  Example 3: 
#  
#  
# Input: p = [1,2,1], q = [1,1,2]
# Output: false
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in both trees is in the range [0, 100]. 
#  -10⁴ <= Node.val <= 10⁴ 
#  
# 
#  Related Topics Tree Depth-First Search Breadth-First Search Binary Tree 👍 74
# 81 👎 157


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        a = []
        b = []

        def inorder(node, order):
            if node:
                inorder(node.left, order)
                order.append(node.val)
                inorder(node.right, order)
            order.append(None)

        inorder(p, a)
        inorder(q, b)

        return a == b

# leetcode submit region end(Prohibit modification and deletion)
