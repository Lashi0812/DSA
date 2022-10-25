#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#
# https://leetcode.com/problems/3sum-closest/description/
#
# algorithms
# Medium (46.21%)
# Likes:    8047
# Dislikes: 445
# Total Accepted:    945.9K
# Total Submissions: 2M
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# Given an integer array nums of length n and an integer target, find three
# integers in nums such that the sum is closest to target.
# 
# Return the sum of the three integers.
# 
# You may assume that each input would have exactly one solution.
# 
# 
# Example 1:
# 
# 
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# 
# 
# Example 2:
# 
# 
# Input: nums = [0,0,0], target = 1
# Output: 0
# Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
# 
# 
# 
# Constraints:
# 
# 
# 3 <= nums.length <= 500
# -1000 <= nums[i] <= 1000
# -10^4 <= target <= 10^4
# 
# 
#

# @lc code=start



from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)-2):
            if i >0 and nums[i]==nums[i-1]:
                continue

            low = i +1
            high = len(nums)-1
            while low < high:
                sums = nums[low] + nums[high] + nums[i]
                if sums == target:
                    return sums

                if abs(sums - target) < abs(result-target):
                    result = sums

                if sums < target:
                    low += 1
                else:
                    high -=1
        return result


        
# @lc code=end
if __name__ == "__main__":
    test = Solution()
    print(test.threeSumClosest([-1,2,1,-4],1))
    print(test.threeSumClosest([0,0,0],1))
