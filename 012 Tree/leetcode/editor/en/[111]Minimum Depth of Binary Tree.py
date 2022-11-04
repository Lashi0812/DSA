# Given a binary tree, find its minimum depth. 
# 
#  The minimum depth is the number of nodes along the shortest path from the 
# root node down to the nearest leaf node. 
# 
#  Note: A leaf is a node with no children. 
# 
#  
#  Example 1: 
#  
#  
# Input: root = [3,9,20,null,null,15,7]
# Output: 2
#  
# 
#  Example 2: 
# 
#  
# Input: root = [2,null,3,null,4,null,5,null,6]
# Output: 5
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [0, 10⁵]. 
#  -1000 <= Node.val <= 1000 
#  
# 
#  Related Topics Tree Depth-First Search Breadth-First Search Binary Tree 👍 50
# 24 👎 1029


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        queue = deque()
        count = 1

        queue.append(root)
        queue.append(None)

        while len(queue) > 1:
            temp = queue.popleft()
            if temp is not None:
                if temp.right is None and temp.left is None:
                    return count
                if temp.left is not None:
                    queue.append(temp.left)
                if temp.right is not None:
                    queue.append(temp.right)
            else:
                queue.append(None)
                count += 1
        return count
# leetcode submit region end(Prohibit modification and deletion)
