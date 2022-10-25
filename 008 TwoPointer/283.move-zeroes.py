#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#
# https://leetcode.com/problems/move-zeroes/description/
#
# algorithms
# Easy (61.31%)
# Likes:    11500
# Dislikes: 286
# Total Accepted:    2M
# Total Submissions: 3.2M
# Testcase Example:  '[0,1,0,3,12]'
#
# Given an integer array nums, move all 0's to the end of it while maintaining
# the relative order of the non-zero elements.
# 
# Note that you must do this in-place without making a copy of the array.
# 
# 
# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:
# Input: nums = [0]
# Output: [0]
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^4
# -2^31 <= nums[i] <= 2^31 - 1
# 
# 
# 
# Follow up: Could you minimize the total number of operations done?
#
from typing import List
# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) :
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for k,v in enumerate(nums):
            if v != 0:
                nums[i],nums[k] = v ,nums[i]
                i += 1
        return nums
            
# if __name__ == "__main__":
#     test = Solution()
#     print(test.moveZeroes([0,1,0,3,12]))
#     print(test.moveZeroes([0]))


        
# @lc code=end

