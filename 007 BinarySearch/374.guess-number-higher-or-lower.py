#
# @lc app=leetcode id=374 lang=python3
#
# [374] Guess Number Higher or Lower
#
# https://leetcode.com/problems/guess-number-higher-or-lower/description/
#
# algorithms
# Easy (50.41%)
# Likes:    1679
# Dislikes: 230
# Total Accepted:    381.1K
# Total Submissions: 756K
# Testcase Example:  '10\n6'
#
# We are playing the Guess Game. The game is as follows:
# 
# I pick a number from 1 to n. You have to guess which number I picked.
# 
# Every time you guess wrong, I will tell you whether the number I picked is
# higher or lower than your guess.
# 
# You call a pre-defined API int guess(int num), which returns three possible
# results:
# 
# 
# -1: Your guess is higher than the number I picked (i.e. num > pick).
# 1: Your guess is lower than the number I picked (i.e. num < pick).
# 0: your guess is equal to the number I picked (i.e. num == pick).
# 
# 
# Return the number that I picked.
# 
# 
# Example 1:
# 
# 
# Input: n = 10, pick = 6
# Output: 6
# 
# 
# Example 2:
# 
# 
# Input: n = 1, pick = 1
# Output: 1
# 
# 
# Example 3:
# 
# 
# Input: n = 2, pick = 1
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 2^31 - 1
# 1 <= pick <= n
# 
# 
#

# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # define the search space
        lowerBound , upperBound = 1,n
        # binary division
        myGuess = (lowerBound+upperBound)>>1
        # walrus operator to assign and return in a single line
        while (res := guess(myGuess)) != 0:
            if res == 1:
                lowerBound = myGuess +1
            else:
                upperBound = myGuess -1
            myGuess = (lowerBound+upperBound)>>1

        return myGuess
                
            
        
# @lc code=end

