#
# @lc app=leetcode id=81 lang=python3
#
# [81] Search in Rotated Sorted Array II
#
# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/
#
# algorithms
# Medium (35.73%)
# Likes:    5254
# Dislikes: 794
# Total Accepted:    469.2K
# Total Submissions: 1.3M
# Testcase Example:  '[2,5,6,0,0,1,2]\n0'
#
# There is an integer array nums sorted in non-decreasing order (not
# necessarily with distinct values).
# 
# Before being passed to your function, nums is rotated at an unknown pivot
# index k (0 <= k < nums.length) such that the resulting array is [nums[k],
# nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For
# example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become
# [4,5,6,6,7,0,1,2,4,4].
# 
# Given the array nums after the rotation and an integer target, return true if
# target is in nums, or false if it is not in nums.
# 
# You must decrease the overall operation steps as much as possible.
# 
# 
# Example 1:
# Input: nums = [2,5,6,0,0,1,2], target = 0
# Output: true
# Example 2:
# Input: nums = [2,5,6,0,0,1,2], target = 3
# Output: false
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 5000
# -10^4 <= nums[i] <= 10^4
# nums is guaranteed to be rotated at some pivot.
# -10^4 <= target <= 10^4
# 
# 
# 
# Follow up: This problem is similar to Search in Rotated Sorted Array, but
# nums may contain duplicates. Would this affect the runtime complexity? How
# and why?
# 
#


from typing import List
# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if len(nums)==1:
            if nums[0]!= target:
                return False
            else:
                return True


        lowerBound = 0 
        upperBound = len(nums)-1

        # shifting to remove duplicate element
        while lowerBound<upperBound and nums[lowerBound] == nums[upperBound] :
            upperBound -= 1


        while lowerBound<=upperBound:
            # # shifting to remove duplicate element
            # while lowerBound<upperBound and nums[lowerBound] == nums[lowerBound+1] :
            #     lowerBound +=1
            # while lowerBound<upperBound and nums[upperBound] == nums[upperBound-1]:
            #     upperBound -= 1

            mid = (lowerBound+upperBound)>>1
            if nums[mid] == target:
                return True
            # on the left side
            if nums[0]<=nums[mid]:
                if target >= nums[0] and target <= nums[mid]:
                    upperBound = mid -1
                else:
                    lowerBound = mid +1
            else:
                if target <= nums[upperBound] and target > nums[mid]:
                    lowerBound = mid +1 
                else:
                    upperBound = mid -1 
        return False
        

if __name__ == "__main__":
    test = Solution()
    print(test.search([2,5,6,0,0,1,2],0))
    print(test.search([2,5,6,0,0,1,2],3))
    print(test.search([1,0,1,1,1],0))
# @lc code=end

