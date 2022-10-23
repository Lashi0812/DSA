#
# @lc app=leetcode id=441 lang=python3
#
# [441] Arranging Coins
#
# https://leetcode.com/problems/arranging-coins/description/
#
# algorithms
# Easy (46.06%)
# Likes:    2749
# Dislikes: 1122
# Total Accepted:    316.9K
# Total Submissions: 688.1K
# Testcase Example:  '5'
#
# You have n coins and you want to build a staircase with these coins. The
# staircase consists of k rows where the i^th row has exactly i coins. The last
# row of the staircase may be incomplete.
# 
# Given the integer n, return the number of complete rows of the staircase you
# will build.
# 
# 
# Example 1:
# 
# 
# Input: n = 5
# Output: 2
# Explanation: Because the 3^rd row is incomplete, we return 2.
# 
# 
# Example 2:
# 
# 
# Input: n = 8
# Output: 3
# Explanation: Because the 4^th row is incomplete, we return 3.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 2^31 - 1
# 
# 
#

# @lc code=start



class Solution1:
    def checkSum(self,num):
        return (num * (num +1))>>1
    def arrangeCoins(self, n: int) -> int:
        lowerBound ,upperBound = 1,n        
        while lowerBound<=upperBound:
            rows = (lowerBound+upperBound)>>1
            if self.checkSum(rows) == n:
                return rows
            if self.checkSum(rows)>n:
                upperBound = rows -1
            else:
                res = rows
                lowerBound = rows+1
        return res

class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int((-1 + (1+8*n) ** 0.5 )//2)



# @lc code=end

