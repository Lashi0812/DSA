#
# @lc app=leetcode id=917 lang=python3
#
# [917] Reverse Only Letters
#
# https://leetcode.com/problems/reverse-only-letters/description/
#
# algorithms
# Easy (61.39%)
# Likes:    1631
# Dislikes: 56
# Total Accepted:    146.5K
# Total Submissions: 238.7K
# Testcase Example:  '"ab-cd"'
#
# Given a string s, reverse the string according to the following rules:
# 
# 
# All the characters that are not English letters remain in the same
# position.
# All the English letters (lowercase or uppercase) should be reversed.
# 
# 
# Return s after reversing it.
# 
# 
# Example 1:
# Input: s = "ab-cd"
# Output: "dc-ba"
# Example 2:
# Input: s = "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"
# Example 3:
# Input: s = "Test1ng-Leet=code-Q!"
# Output: "Qedo1ct-eeLg=ntse-T!"
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 100
# s consists of characters with ASCII values in the range [33, 122].
# s does not contain '\"' or '\\'.
# 
# 
#

# @lc code=start
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        st = list(s)
        l = 0
        r = len(st)-1
        while l < r:
            while l<r and not st[l].isalpha():
                l +=1
            while l<r and not st[r].isalpha():
                r -=1
            st[l],st[r] = st[r],st[l]
            l +=1
            r -=1
        return "".join(st)
        
# @lc code=end

