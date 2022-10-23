#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#
# https://leetcode.com/problems/search-insert-position/description/
#
# algorithms
# Easy (42.00%)
# Likes:    10235
# Dislikes: 481
# Total Accepted:    1.8M
# Total Submissions: 4.2M
# Testcase Example:  '[1,3,5,6]\n5'
#
# Given a sorted array of distinct integers and a target value, return the
# index if the target is found. If not, return the index where it would be if
# it were inserted in order.
# 
# You must write an algorithm with O(log n) runtime complexity.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,3,5,6], target = 5
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,3,5,6], target = 2
# Output: 1
# 
# 
# Example 3:
# 
# 
# Input: nums = [1,3,5,6], target = 7
# Output: 4
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^4
# -10^4 <= nums[i] <= 10^4
# nums contains distinct values sorted in ascending order.
# -10^4 <= target <= 10^4
# 
# 
#

# @lc code=start


from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return l


if __name__ == "__main__":
    test = Solution()
    print(test.searchInsert([1, 3, 5, 6], 7))
    print(test.searchInsert([1,3,5,6],2))
    print(test.searchInsert([1,3,5,6],5))

# @lc code=end
