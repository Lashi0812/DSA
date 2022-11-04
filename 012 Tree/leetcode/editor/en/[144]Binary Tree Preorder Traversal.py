# Given the root of a binary tree, return the preorder traversal of its nodes' 
# values. 
# 
#  
#  Example 1: 
#  
#  
# Input: root = [1,null,2,3]
# Output: [1,2,3]
#  
# 
#  Example 2: 
# 
#  
# Input: root = []
# Output: []
#  
# 
#  Example 3: 
# 
#  
# Input: root = [1]
# Output: [1]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [0, 100]. 
#  -100 <= Node.val <= 100 
#  
# 
#  
#  Follow up: Recursive solution is trivial, could you do it iteratively? 
# 
#  Related Topics Stack Tree Depth-First Search Binary Tree 👍 5288 👎 144


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        order = []

        def _preorder(node):
            if node is None:
                return
            order.append(node.val)
            _preorder(node.left)
            _preorder(node.right)

        _preorder(root)

        return order
# leetcode submit region end(Prohibit modification and deletion)
