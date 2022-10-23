#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#
# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
#
# algorithms
# Medium (38.62%)
# Likes:    18166
# Dislikes: 1083
# Total Accepted:    1.8M
# Total Submissions: 4.6M
# Testcase Example:  '[4,5,6,7,0,1,2]\n0'
#
# There is an integer array nums sorted in ascending order (with distinct
# values).
# 
# Prior to being passed to your function, nums is possibly rotated at an
# unknown pivot index k (1 <= k < nums.length) such that the resulting array is
# [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]
# (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3
# and become [4,5,6,7,0,1,2].
# 
# Given the array nums after the possible rotation and an integer target,
# return the index of target if it is in nums, or -1 if it is not in nums.
# 
# You must write an algorithm with O(log n) runtime complexity.
# 
# 
# Example 1:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:
# Input: nums = [1], target = 0
# Output: -1
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 5000
# -10^4 <= nums[i] <= 10^4
# All values of nums are unique.
# nums is an ascending array that is possibly rotated.
# -10^4 <= target <= 10^4
# 
# 
#


# @lc code=start

from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lowerBound = 0
        upperBound = len(nums)-1
        while lowerBound<=upperBound:
            mid = (lowerBound+upperBound)>>1
            if nums[mid] == target:
                return mid
            # on the left part 
            if nums[0] <= nums[mid]:
                #reduce the space
                if target >= nums[0] and nums[mid] > target:
                    upperBound = mid -1
                else:
                    lowerBound = mid+1
            else:
                if target <= nums[-1] and target > nums[mid]:
                    lowerBound = lowerBound +1
                else:
                    upperBound = upperBound -1
        return -1



        
# @lc code=end

