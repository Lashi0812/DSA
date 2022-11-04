# Given the root of a binary tree, check whether it is a mirror of itself (i.e.,
#  symmetric around its center). 
# 
#  
#  Example 1: 
#  
#  
# Input: root = [1,2,2,3,4,4,3]
# Output: true
#  
# 
#  Example 2: 
#  
#  
# Input: root = [1,2,2,null,3,null,3]
# Output: false
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [1, 1000]. 
#  -100 <= Node.val <= 100 
#  
# 
#  
# Follow up: Could you solve it both recursively and iteratively?
# 
#  Related Topics Tree Depth-First Search Breadth-First Search Binary Tree 👍 11
# 475 👎 260


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def compare(left, right):
            if left is None and right is None:
                return True
            elif left and right and (left.val == right.val):
                return compare(left.left, right.right) and compare(left.right,right.left)
            else:
                return False

        return compare(root.left, root.right)

# leetcode submit region end(Prohibit modification and deletion)
