# Given the root of a binary tree, construct a string consisting of parenthesis 
# and integers from a binary tree with the preorder traversal way, and return it. 
# 
# 
#  Omit all the empty parenthesis pairs that do not affect the one-to-one 
# mapping relationship between the string and the original binary tree. 
# 
#  
#  Example 1: 
#  
#  
# Input: root = [1,2,3,4]
# Output: "1(2(4))(3)"
# Explanation: Originally, it needs to be "1(2(4)())(3()())", but you need to 
# omit all the unnecessary empty parenthesis pairs. And it will be "1(2(4))(3)"
#  
# 
#  Example 2: 
#  
#  
# Input: root = [1,2,3,null,4]
# Output: "1(2()(4))(3)"
# Explanation: Almost the same as the first example, except we cannot omit the 
# first parenthesis pair to break the one-to-one mapping relationship between the 
# input and the output.
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [1, 10⁴]. 
#  -1000 <= Node.val <= 1000 
#  
# 
#  Related Topics String Tree Depth-First Search Binary Tree 👍 2382 👎 2886


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution(object):
    def tree2str(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """

        def _inorder(node):
            if node is None:
                return
            # todo
            _inorder(node.left)
            _inorder(node.right)


# leetcode submit region end(Prohibit modification and deletion)
