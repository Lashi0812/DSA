#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
#
# algorithms
# Medium (41.49%)
# Likes:    14407
# Dislikes: 353
# Total Accepted:    1.4M
# Total Submissions: 3.3M
# Testcase Example:  '[5,7,7,8,8,10]\n8'
#
# Given an array of integers nums sorted in non-decreasing order, find the
# starting and ending position of a given target value.
# 
# If target is not found in the array, return [-1, -1].
# 
# You must write an algorithm with O(log n) runtime complexity.
# 
# 
# Example 1:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:
# Input: nums = [], target = 0
# Output: [-1,-1]
# 
# 
# Constraints:
# 
# 
# 0 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# nums is a non-decreasing array.
# -10^9 <= target <= 10^9
# 
# 
#

# @lc code=start
from typing import List

class Solution:
    def occurance(self,which,nums,target):
        lowerBound,upperBound = 0,len(nums)-1
        occ =-1
        while lowerBound<=upperBound:
            
            mid = (lowerBound+upperBound)>>1
            
            if nums[mid]==target:
                occ = mid
                if which == "first":
                    upperBound = mid -1
                else:
                    lowerBound = mid +1

            if nums[mid]<target:
                lowerBound = mid +1
            elif nums[mid]>target:
                upperBound = mid -1
            
        return occ

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first_occ = self.occurance("first",nums,target)
        if first_occ == -1:
            return [-1,-1]
       
        last_occ = self.occurance("last",nums,target)
        return [first_occ,last_occ]
        
# if __name__ == "__main__":
#     test = Solution()
#     print(test.searchRange([5,7,7,8,8,10],8))
#     print(test.searchRange([5,7,7,8,8,10],6))
#     print(test.searchRange([2,2],2))
# @lc code=end

