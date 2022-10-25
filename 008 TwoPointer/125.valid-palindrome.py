#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#
# https://leetcode.com/problems/valid-palindrome/description/
#
# algorithms
# Easy (43.48%)
# Likes:    5140
# Dislikes: 6171
# Total Accepted:    1.6M
# Total Submissions: 3.7M
# Testcase Example:  '"A man, a plan, a canal: Panama"'
#
# A phrase is a palindrome if, after converting all uppercase letters into
# lowercase letters and removing all non-alphanumeric characters, it reads the
# same forward and backward. Alphanumeric characters include letters and
# numbers.
# 
# Given a string s, return true if it is a palindrome, or false otherwise.
# 
# 
# Example 1:
# 
# 
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# 
# 
# Example 2:
# 
# 
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# 
# 
# Example 3:
# 
# 
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric
# characters.
# Since an empty string reads the same forward and backward, it is a
# palindrome.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 2 * 10^5
# s consists only of printable ASCII characters.
# 
# 
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1
        while l<r:
            # remove the non-alpha numeric on left 
            while l<r and not s[l].isalnum():
                l += 1

            while l<r and not s[r].isalnum():
                r -=1
            
            if s[l].lower() != s[r].lower():
                return False
            l +=1
            r -=1
        return True

        
# @lc code=end


# if __name__ == "__main__":
#     test = Solution()
#     print(test.isPalindrome("A man, a plan, a canal: Panama"))
#     print(test.isPalindrome("race a car"))
#     print(test.isPalindrome(" "))
