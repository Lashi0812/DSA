#
# @lc app=leetcode id=344 lang=python3
#
# [344] Reverse String
#
# https://leetcode.com/problems/reverse-string/description/
#
# algorithms
# Easy (76.08%)
# Likes:    6298
# Dislikes: 1012
# Total Accepted:    1.8M
# Total Submissions: 2.4M
# Testcase Example:  '["h","e","l","l","o"]'
#
# Write a function that reverses a string. The input string is given as an
# array of characters s.
# 
# You must do this by modifying the input array in-place with O(1) extra
# memory.
# 
# 
# Example 1:
# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:
# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^5
# s[i] is a printable ascii character.
# 
# 
#

from typing import List
# @lc code=start
class Solution:
    def reverseString(self, s: List[str]):
        """
        Do not return anything, modify s in-place instead.
        """
        l ,r = 0 ,len(s)-1
        while l <r:
            s[l],s[r] = s[r],s[l]
            l += 1
            r -= 1
        return s

# if __name__ == "__main__":
#     test = Solution()
#     print(test.reverseString(["h","e","l","l","o"]))
#     print(test.reverseString(["H","a","n","n","a","h"]))
        
# @lc code=end

