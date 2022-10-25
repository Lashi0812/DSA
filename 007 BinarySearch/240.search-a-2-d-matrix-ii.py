#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#
# https://leetcode.com/problems/search-a-2d-matrix-ii/description/
#
# algorithms
# Medium (50.53%)
# Likes:    9444
# Dislikes: 158
# Total Accepted:    727.5K
# Total Submissions: 1.4M
# Testcase Example:  '[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]\n' +
#  '5'
#
# Write an efficient algorithm that searches for a value target in an m x n
# integer matrix matrix. This matrix has the following properties:
# 
# 
# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
# 
# 
# 
# Example 1:
# 
# 
# Input: matrix =
# [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],
# target = 5
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: matrix =
# [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],
# target = 20
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# m == matrix.length
# n == matrix[i].length
# 1 <= n, m <= 300
# -10^9 <= matrix[i][j] <= 10^9
# All the integers in each row are sorted in ascending order.
# All the integers in each column are sorted in ascending order.
# -10^9 <= target <= 10^9
# 
# 
#

# @lc code=start
from typing import List

class Solution:

    # def binary_search(self,matrix,target,row_mid,col_mid,dir):
    #   lowerBound = 0
    #   upperBound = col_mid if dir =="row" else row_mid
    #   while lowerBound<=upperBound:
    #     middle = (lowerBound+upperBound)>>1
    #     temp = matrix[row_mid if dir == "row" else middle][middle if dir == "row" else col_mid]
    #     if temp == target:
    #       return True
    #     elif temp < target:
    #       lowerBound = lowerBound +1
    #     else:
    #       upperBound = upperBound -1
    #   return False
    
    def searchMatrix(self,matrix, target):
      m, n = len(matrix), len(matrix) and len(matrix[0])
      r, c = 0, n-1
      while r < m and c >= 0:
        if target > matrix[r][c]:
          r += 1
        elif target < matrix[r][c]:
          c -= 1
        else: return True
      return False

      




      # lowerBound = 0
      # upperBound = len(nums)-1
      # while lowerBound<=upperBound:
      #   mid = (lowerBound+upperBound)>>1
      #   if nums[mid]==target:
      #     return True
      #   elif nums[mid]>target:
      #     upperBound = mid -1
      #   else:
      #     lowerBound = mid +1
      # return False







    # def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    #   row_lb,row_ub = 0,len(matrix)-1
    #   col_lb,col_ub = 0,len(matrix[0])-1
    #   while row_lb<=row_ub or col_lb<=col_ub:
        
    #     row_mid = (row_lb+row_ub)>>1
    #     col_mid = (col_lb+col_ub)>>1
        

    #     if matrix[row_mid][col_mid]==target:
    #       return True

    #     # reduce the search space
    #     elif matrix[row_mid][col_mid]<target:
    #       row_lb = row_mid +1
    #       col_lb = col_mid +1

    #     else:
    #       # row binary search
    #       if self.binary_search(matrix,target,row_mid,col_mid,"row") or self.binary_search(matrix,target,row_mid,col_mid,"col"):
    #         return True
    #       row_ub = row_mid -1
    #       col_ub = col_mid -1
      
    #   return False

# if __name__ == "__main__":
#   test = Solution()
#   print(test.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],5))
#   print(test.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],22))
  


          


        
# @lc code=end

