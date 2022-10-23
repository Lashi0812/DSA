#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#
# https://leetcode.com/problems/minimum-size-subarray-sum/description/
#
# algorithms
# Medium (44.42%)
# Likes:    8097
# Dislikes: 224
# Total Accepted:    619K
# Total Submissions: 1.4M
# Testcase Example:  '7\n[2,3,1,2,4,3]'
#
# Given an array of positive integers nums and a positive integer target,
# return the minimal length of a contiguous subarray [numsl, numsl+1, ...,
# numsr-1, numsr] of which the sum is greater than or equal to target. If there
# is no such subarray, return 0 instead.
# 
# 
# Example 1:
# 
# 
# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem
# constraint.
# 
# 
# Example 2:
# 
# 
# Input: target = 4, nums = [1,4,4]
# Output: 1
# 
# 
# Example 3:
# 
# 
# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# 1 <= target <= 10^9
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^4
# 
# 
# 
# Follow up: If you have figured out the O(n) solution, try coding another
# solution of which the time complexity is O(n log(n)).
#
from typing import List
# @lc code=start
class Solution:
    def sums(self,nums,mid,target):
        temp = 0 
        # Calculate the first window
        for i in range(mid):
            temp += nums[i]        
        
        for i in range(0,len(nums)-mid):
            temp = temp - nums[i] + nums[i+mid]
            if temp > target:
                break
        return temp
                
        


    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # target => minimum size of array
        # define the search space
        lowerBound = 1
        upperBound = len(nums)
        ans = 0
        

        while lowerBound<=upperBound:
            mid = (lowerBound+upperBound)>>1
            temp = self.sums(nums,mid,target)
            if temp>target:                             
                upperBound = mid -1
            else:
                ans = mid
                lowerBound = mid +1
        return ans
        

if __name__ == "__main__":
    test = Solution()
    print(test.minSubArrayLen(7,[2,3,1,2,4,3]))
    print(test.minSubArrayLen(4,[1,4,4]))
    print(test.minSubArrayLen(11,[1,1,1,1,1,1,1,1]))
    print(test.minSubArrayLen(11,[1,2,3,4,5]))
# @lc code=end

