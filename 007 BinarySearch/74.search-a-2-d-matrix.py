#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#
# https://leetcode.com/problems/search-a-2d-matrix/description/
#
# algorithms
# Medium (46.77%)
# Likes:    10138
# Dislikes: 310
# Total Accepted:    1M
# Total Submissions: 2.2M
# Testcase Example:  '[[1,3,5,7],[10,11,16,20],[23,30,34,60]]\n3'
#
# Write an efficient algorithm that searches for a value target in an m x n
# integer matrix matrix. This matrix has the following properties:
# 
# 
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the
# previous row.
# 
# 
# 
# Example 1:
# 
# 
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -10^4 <= matrix[i][j], target <= 10^4
# 
# 
#

# @lc code=start

from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or target is None:
            return False

        rows,cols = len(matrix),len(matrix[0])
        lowerbound ,upperBound = 0, rows * cols -1



        while lowerbound<=upperBound:
            mid = (lowerbound+upperBound)>>1
            num = matrix[mid//cols][mid%cols]
            if num == target:
                return True
            elif num < target:
                lowerbound = mid +1
            else:
                upperBound = upperBound -1
        return False

if __name__ == "__main__":
    test = Solution()
    print(test.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],13))
    print(test.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],20))
    print(test.searchMatrix([[1],[3]],3))




        
# @lc code=end

