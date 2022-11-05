# Given the root of a binary tree, return the average value of the nodes on 
# each level in the form of an array. Answers within 10⁻⁵ of the actual answer will 
# be accepted.
# 
#  
#  Example 1: 
#  
#  
# Input: root = [3,9,20,null,null,15,7]
# Output: [3.00000,14.50000,11.00000]
# Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, 
# and on level 2 is 11.
# Hence return [3, 14.5, 11].
#  
# 
#  Example 2: 
#  
#  
# Input: root = [3,9,20,15,7]
# Output: [3.00000,14.50000,11.00000]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [1, 10⁴]. 
#  -2³¹ <= Node.val <= 2³¹ - 1 
#  
# 
#  Related Topics Tree Depth-First Search Breadth-First Search Binary Tree 👍 43
# 78 👎 276


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """

        def _level_order_traversal(node):
            if node is None:
                return []
            q = deque()
            q.append(root)
            q.append(None)
            ans = []
            level_sum = 0
            count = 0
            while q:
                temp = q.popleft()
                if temp is not None:
                    level_sum += temp.val
                    count += 1
                    if temp.left is not None:
                        q.append(temp.left)
                    if temp.right is not None:
                        q.append(temp.right)
                else:
                    # compute the average
                    avg = float(level_sum) / count
                    ans.append(avg)
                    level_sum = 0
                    count = 0
                    if q:
                        q.append(None)
            return ans

        return _level_order_traversal(root)
# leetcode submit region end(Prohibit modification and deletion)
