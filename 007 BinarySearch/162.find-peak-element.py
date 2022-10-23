#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#
# https://leetcode.com/problems/find-peak-element/description/
#
# algorithms
# Medium (46.19%)
# Likes:    7641
# Dislikes: 4068
# Total Accepted:    908.7K
# Total Submissions: 2M
# Testcase Example:  '[1,2,3,1]'
#
# A peak element is an element that is strictly greater than its neighbors.
# 
# Given a 0-indexed integer array nums, find a peak element, and return its
# index. If the array contains multiple peaks, return the index to any of the
# peaks.
# 
# You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is
# always considered to be strictly greater than a neighbor that is outside the
# array.
# 
# You must write an algorithm that runs in O(log n) time.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index
# number 2.
# 
# Example 2:
# 
# 
# Input: nums = [1,2,1,3,5,6,4]
# Output: 5
# Explanation: Your function can return either index number 1 where the peak
# element is 2, or index number 5 where the peak element is 6.
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 1000
# -2^31 <= nums[i] <= 2^31 - 1
# nums[i] != nums[i + 1] for all valid i.
# 
# 
#

# @lc code=start

from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # handle the boundary case
        if len(nums) == 1: return 0 
        if nums[0]>nums[1] : return 0
        if nums[-1]>nums[-2]: return len(nums)-1
        

        lowerBound = 0 
        upperBound = len(nums)-1
        ans = -1
        while lowerBound <= upperBound:
            mid = (lowerBound+upperBound)>>1
            # case 1
            if nums[mid-1]<nums[mid]>nums[mid]:
                return mid 
            # case 2 
            if nums[mid+1]>nums[mid]:
                lowerBound = mid + 1
            else:
                ans = mid
                upperBound = mid -1
        return ans
if __name__ == "__main__":
    test = Solution()
    print(test.findPeakElement([1,2,3,1]))      
    print(test.findPeakElement([1,2,1,3,5,6,4]))
    print(test.findPeakElement([3,1,2,4]))
    print(test.findPeakElement([1]))
    print(test.findPeakElement([1,2]))    
    
            
        
# @lc code=end

