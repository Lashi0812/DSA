# Given the root of a Binary Search Tree (BST), return the minimum difference 
# between the values of any two different nodes in the tree. 
# 
#  
#  Example 1: 
#  
#  
# Input: root = [4,2,6,1,3]
# Output: 1
#  
# 
#  Example 2: 
#  
#  
# Input: root = [1,0,48,null,null,12,49]
# Output: 1
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [2, 100]. 
#  0 <= Node.val <= 10⁵ 
#  
# 
#  
#  Note: This question is the same as 530: https://leetcode.com/problems/
# minimum-absolute-difference-in-bst/ 
# 
#  Related Topics Tree Depth-First Search Breadth-First Search Binary Search 
# Tree Binary Tree 👍 1915 👎 336


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.prev = None
        self.min_diff = float("inf")
        self._inorder(root)
        return self.min_diff

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            if self.prev is None:
                self.prev = node
            else:
                diff = node.val - self.prev.val
                self.min_diff = min(self.min_diff, diff)
                self.prev = node
            self._inorder(node.right)

# leetcode submit region end(Prohibit modification and deletion)
