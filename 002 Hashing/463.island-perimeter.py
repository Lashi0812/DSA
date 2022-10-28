#
# @lc app=leetcode id=463 lang=python3
#
# [463] Island Perimeter
#
# https://leetcode.com/problems/island-perimeter/description/
#
# algorithms
# Easy (69.44%)
# Likes:    5077
# Dislikes: 257
# Total Accepted:    401.5K
# Total Submissions: 578K
# Testcase Example:  '[[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]'
#
# You are given row x col grid representing a map where grid[i][j] = 1
# represents land and grid[i][j] = 0 represents water.
# 
# Grid cells are connected horizontally/vertically (not diagonally). The grid
# is completely surrounded by water, and there is exactly one island (i.e., one
# or more connected land cells).
# 
# The island doesn't have "lakes", meaning the water inside isn't connected to
# the water around the island. One cell is a square with side length 1. The
# grid is rectangular, width and height don't exceed 100. Determine the
# perimeter of the island.
# 
# 
# Example 1:
# 
# 
# Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
# Output: 16
# Explanation: The perimeter is the 16 yellow stripes in the image above.
# 
# 
# Example 2:
# 
# 
# Input: grid = [[1]]
# Output: 4
# 
# 
# Example 3:
# 
# 
# Input: grid = [[1,0]]
# Output: 4
# 
# 
# 
# Constraints:
# 
# 
# row == grid.length
# col == grid[i].length
# 1 <= row, col <= 100
# grid[i][j] is 0 or 1.
# There is exactly one island in grid.
# 
# 
#
from turtle import right
from typing import List
# @lc code=start
class Solution:


    def islandPerimeter1(self, grid: List[List[int]]) -> int:
        total_col = len(grid[0])
        size = len(grid) * total_col

        numberOfLand = 0 
        sharedBoundary = 0
        for i in range(size):
            # if i in the land
            row,col = divmod(i,total_col)
            if grid[row][col] == 1:
                numberOfLand += 1

                # find the shared Boundary

                # left side ==> check for same row
                left = i - 1
                l_row,l_col = divmod(left,total_col)
                if row == l_row:
                    if grid[l_row][l_col] == 1:
                        sharedBoundary += 1
                
                # right side ==> check for same row
                right = i + 1
                r_row ,r_col = divmod(right,total_col)
                if row == r_row:
                    if grid[r_row][r_col] == 1:
                        sharedBoundary += 1
                
                # up side ==> check for boundary
                up = i - total_col
                u_row ,u_col = divmod(up,total_col)
                if up >= 0:
                    if grid[u_row][u_col] == 1:
                        sharedBoundary += 1

                # down side ==> check for the boundary
                down = i + total_col
                d_row,d_col = divmod(down,total_col)
                if down < size:
                    if grid[d_row][d_col] == 1:
                        sharedBoundary += 1

        return (4 * numberOfLand )- sharedBoundary

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        perimeter = 0

        for row in range(m):
            for col in range(n):
                perimeter += 4 * grid[row][col]

                # up
                if row>0   : perimeter -= grid[row][col] * grid[row-1][col]  
                # down
                if row<m-1 : perimeter -= grid[row][col] * grid[row+1][col]
                # left
                if col>0   : perimeter -= grid[row][col] * grid[row][col-1]
                # right
                if col<n-1 : perimeter -= grid[row][col] * grid[row][col+1]
        return perimeter

                
if __name__ == "__main__":
    test = Solution()
    grid1 = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
    grid2 = [[1]]
    grid3 = [[1,0]]
    print(test.islandPerimeter1(grid1))
    print(test.islandPerimeter1(grid2))
    print(test.islandPerimeter1(grid3))





        
# @lc code=end

