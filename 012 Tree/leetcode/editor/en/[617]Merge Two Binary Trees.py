# You are given two binary trees root1 and root2. 
# 
#  Imagine that when you put one of them to cover the other, some nodes of the 
# two trees are overlapped while the others are not. You need to merge the two 
# trees into a new binary tree. The merge rule is that if two nodes overlap, then sum 
# node values up as the new value of the merged node. Otherwise, the NOT null 
# node will be used as the node of the new tree. 
# 
#  Return the merged tree. 
# 
#  Note: The merging process must start from the root nodes of both trees. 
# 
#  
#  Example 1: 
#  
#  
# Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
# Output: [3,4,5,5,4,null,7]
#  
# 
#  Example 2: 
# 
#  
# Input: root1 = [1], root2 = [1,2]
# Output: [2,2]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in both trees is in the range [0, 2000]. 
#  -10⁴ <= Node.val <= 10⁴ 
#  
# 
#  Related Topics Tree Depth-First Search Breadth-First Search Binary Tree 👍 74
# 89 👎 263


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        if root1 is None:
            return root2
        elif root2 is None:
            return root1
        elif root1 is None and root2 is None:
            return

        def _preoder(node1, node2):
            # access the value
            if node1 is not None and node2 is not None and node1 != node2:
                node1.val = node2.val + node1.val
            if node1.left is None and node2.left is not None:
                node1.left = node2.left
            if node1.right is None and node2.right is not None:
                node1.right = node2.right

            if node1.left is not None and node2.left is not None:
                _preoder(node1.left, node2.left)

            if node1.right is not None and node2.right is not None:
                _preoder(node1.right, node2.right)

        _preoder(root1, root2)
        return root1
# leetcode submit region end(Prohibit modification and deletion)
