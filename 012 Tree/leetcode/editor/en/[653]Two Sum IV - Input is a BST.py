# Given the root of a Binary Search Tree and a target number k, return true if 
# there exist two elements in the BST such that their sum is equal to the given 
# target. 
# 
#  
#  Example 1: 
#  
#  
# Input: root = [5,3,6,2,4,null,7], k = 9
# Output: true
#  
# 
#  Example 2: 
#  
#  
# Input: root = [5,3,6,2,4,null,7], k = 28
# Output: false
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [1, 10⁴]. 
#  -10⁴ <= Node.val <= 10⁴ 
#  root is guaranteed to be a valid binary search tree. 
#  -10⁵ <= k <= 10⁵ 
#  
# 
#  Related Topics Hash Table Two Pointers Tree Depth-First Search Breadth-First 
# Search Binary Search Tree Binary Tree 👍 5324 👎 231


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """

        hashset = set()

        def _preorder(node, is_there=False, target=k):
            if node is None:
                return False

            need = k - node.val
            if need in hashset:
                is_there = True
            else:
                hashset.add(node.val)
            if not is_there:
                is_there = _preorder(node.left, is_there)
            if not is_there:
                is_there = _preorder(node.right, is_there)
            return is_there

        return _preorder(root)

        # Without Extra space
        # def search(cur_node, node, target):
        #     while node is not None:
        #         print("searching at ", node.val)
        #         if cur_node != node and node.val == target:
        #             return True
        #         elif node.val > target:
        #             node = node.left
        #         else:
        #             node = node.right
        #     return False
        #
        # def _preorder(node, is_there=False, target=k):
        #     if node is None:
        #         return
        #     else:
        #         print(node.val)
        #         is_there = search(node, root, k - node.val)
        #         if not is_there:
        #             is_there = _preorder(node.left, is_there)
        #         if not is_there:
        #             is_there = _preorder(node.right, is_there)
        #         return is_there
        #
        # return _preorder(root)

        # leetcode submit region end(Prohibit modification and deletion)
