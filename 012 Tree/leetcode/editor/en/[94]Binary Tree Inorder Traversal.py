# Given the root of a binary tree, return the inorder traversal of its nodes' 
# values. 
# 
#  
#  Example 1: 
#  
#  
# Input: root = [1,null,2,3]
# Output: [1,3,2]
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
# Follow up: Recursive solution is trivial, could you do it iteratively?
# 
#  Related Topics Stack Tree Depth-First Search Binary Tree 👍 10054 👎 476


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []

        def _inorder(node):
            nonlocal ans
            if node is None:
                return
            # go to left
            _inorder(node.left)
            # access the data
            ans.append(node.val)
            # go to right
            _inorder(node.right)

        _inorder(root)
        return ans

# leetcode submit region end(Prohibit modification and deletion)
