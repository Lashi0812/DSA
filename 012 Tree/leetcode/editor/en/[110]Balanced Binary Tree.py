# Given a binary tree, determine if it is height-balanced. 
# 
#  
#  Example 1: 
#  
#  
# Input: root = [3,9,20,null,null,15,7]
# Output: true
#  
# 
#  Example 2: 
#  
#  
# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
#  
# 
#  Example 3: 
# 
#  
# Input: root = []
# Output: true
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [0, 5000]. 
#  -10⁴ <= Node.val <= 10⁴ 
#  
# 
#  Related Topics Tree Depth-First Search Binary Tree 👍 7663 👎 411


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def check(left, right):
            if abs(left - right) > 1:
                return False
            else:
                return True

        def height(node, is_bst=True):
            if node is None:
                return 0, is_bst
            left, is_bst = height(node.left, is_bst)
            right, is_bst = height(node.right, is_bst)
            is_bst = check(left, right) and is_bst
            return max(left, right) + 1, is_bst

        depth, ans = height(root)
        return ans
    # leetcode submit region end(Prohibit modification and deletion)
