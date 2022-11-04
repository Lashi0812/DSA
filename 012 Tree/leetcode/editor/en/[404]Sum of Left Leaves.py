# Given the root of a binary tree, return the sum of all left leaves. 
# 
#  A leaf is a node with no children. A left leaf is a leaf that is the left 
# child of another node. 
# 
#  
#  Example 1: 
#  
#  
# Input: root = [3,9,20,null,null,15,7]
# Output: 24
# Explanation: There are two left leaves in the binary tree, with values 9 and 1
# 5 respectively.
#  
# 
#  Example 2: 
# 
#  
# Input: root = [1]
# Output: 0
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [1, 1000]. 
#  -1000 <= Node.val <= 1000 
#  
# 
#  Related Topics Tree Depth-First Search Breadth-First Search Binary Tree 👍 39
# 81 👎 263


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def _preorder(node, prev=None, tot=0):
            if node is None:
                return prev, tot
            else:
                if prev is not None and prev.left == node and node.left is None and node.right is None:
                    tot += node.val
                prev = node
                prev, tot = _preorder(node.left, prev, tot)
                prev, tot = _preorder(node.right, prev, tot)
                return prev, tot

        last, ans = _preorder(root)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
