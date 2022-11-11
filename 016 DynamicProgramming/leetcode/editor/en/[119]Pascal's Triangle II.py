# Given an integer rowIndex, return the rowIndexᵗʰ (0-indexed) row of the 
# Pascal's triangle. 
# 
#  In Pascal's triangle, each number is the sum of the two numbers directly 
# above it as shown: 
#  
#  
#  Example 1: 
#  Input: rowIndex = 3
# Output: [1,3,3,1]
#  
#  Example 2: 
#  Input: rowIndex = 0
# Output: [1]
#  
#  Example 3: 
#  Input: rowIndex = 1
# Output: [1,1]
#  
#  
#  Constraints: 
# 
#  
#  0 <= rowIndex <= 33 
#  
# 
#  
#  Follow up: Could you optimize your algorithm to use only O(rowIndex) extra 
# space? 
# 
#  Related Topics Array Dynamic Programming 👍 3280 👎 285


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        ans = [1]
        for col in range(1, rowIndex + 1):
            ans.append((ans[col - 1] * (rowIndex - col + 1)) // col)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


