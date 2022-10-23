#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#
# https://leetcode.com/problems/valid-perfect-square/description/
#
# algorithms
# Easy (43.26%)
# Likes:    2936
# Dislikes: 253
# Total Accepted:    425.9K
# Total Submissions: 984.5K
# Testcase Example:  '16'
#
# Given a positive integer num, write a function which returns True if num is a
# perfect square else False.
# 
# Follow up: Do not use any built-in library function such as sqrt.
# 
# 
# Example 1:
# Input: num = 16
# Output: true
# Example 2:
# Input: num = 14
# Output: false
# 
# 
# Constraints:
# 
# 
# 1 <= num <= 2^31 - 1
# 
# 
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = 1 
        r = num
        while l<=r:
            mid = (l+r)//2
            temp = mid * mid
            if temp == num:
                return True
            if temp < num:
                l = mid +1
            else:
                r = mid -1
        return False
        
# @lc code=end
if __name__ == "__main__":
    test = Solution()
    print(test.isPerfectSquare(16))
    print(test.isPerfectSquare(17))