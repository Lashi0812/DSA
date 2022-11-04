# Given the root of a Binary Search Tree (BST), return the minimum absolute 
# difference between the values of any two different nodes in the tree. 
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
#  The number of nodes in the tree is in the range [2, 10⁴]. 
#  0 <= Node.val <= 10⁵ 
#  
# 
#  
#  Note: This question is the same as 783: https://leetcode.com/problems/
# minimum-distance-between-bst-nodes/ 
# 
#  Related Topics Tree Depth-First Search Breadth-First Search Binary Search 
# Tree Binary Tree 👍 2461 👎 132


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def moris_traversal(node):
            cur = node
            prev = None
            mini = float("inf")
            while cur is not None:
                if cur.left is None:
                    if prev is not None:
                        mini = min(mini, abs(prev.val - cur.val))
                    prev = cur
                    cur = cur.right
                else:
                    # find the inorder predecessor
                    inorder_predecessor = cur.left
                    while inorder_predecessor.right is not None and inorder_predecessor.right != cur:
                        inorder_predecessor = inorder_predecessor.right
                    if inorder_predecessor.right is None:
                        inorder_predecessor.right = cur
                        cur = cur.left
                    else:
                        inorder_predecessor.right = None
                        if prev is not None:
                            mini = min(mini, abs(prev.val - cur.val))
                        prev = cur
                        cur = cur.right
            return mini
        return moris_traversal(root)
# leetcode submit region end(Prohibit modification and deletion)
