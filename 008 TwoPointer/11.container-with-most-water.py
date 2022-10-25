#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#
# https://leetcode.com/problems/container-with-most-water/description/
#
# algorithms
# Medium (54.31%)
# Likes:    20871
# Dislikes: 1106
# Total Accepted:    1.8M
# Total Submissions: 3.3M
# Testcase Example:  '[1,8,6,2,5,4,8,3,7]'
#
# You are given an integer array height of length n. There are n vertical lines
# drawn such that the two endpoints of the i^th line are (i, 0) and (i,
# height[i]).
# 
# Find two lines that together with the x-axis form a container, such that the
# container contains the most water.
# 
# Return the maximum amount of water a container can store.
# 
# Notice that you may not slant the container.
# 
# 
# Example 1:
# 
# 
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array
# [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the
# container can contain is 49.
# 
# 
# Example 2:
# 
# 
# Input: height = [1,1]
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# n == height.length
# 2 <= n <= 10^5
# 0 <= height[i] <= 10^4
# 
# 
#

# @lc code=start


from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1
        area = 0
        while i<j:
            area = max(area,(j-i) * min(height[i],height[j]) )
            if height[i]<=height[j]:
                i +=1 
            else:
                j -=1

        return area
# @lc code=end

if __name__ =="__main__":
    test = Solution()
    print(test.maxArea([1,8,6,2,5,4,8,3,7]))
    print(test.maxArea([1,1]))


