#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#
# https://leetcode.com/problems/reverse-vowels-of-a-string/description/
#
# algorithms
# Easy (47.68%)
# Likes:    1985
# Dislikes: 2028
# Total Accepted:    389.3K
# Total Submissions: 816.3K
# Testcase Example:  '"hello"'
#
# Given a string s, reverse only all the vowels in the string and return it.
# 
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower
# and upper cases, more than once.
# 
# 
# Example 1:
# Input: s = "hello"
# Output: "holle"
# Example 2:
# Input: s = "leetcode"
# Output: "leotcede"
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 3 * 10^5
# s consist of printable ASCII characters.
# 
# 
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        st = list(s)
        l = 0
        r = len(st)-1
        while l<r:
            # move the left pointer to the vowel
            while l<r and st[l] not in "aeiouAEIOU":
                l +=1
            while l<r and st[r] not in "aeiouAEIOU":
                r -=1

            st[l],st[r] = st[r],st[l]
            l +=1
            r -=1

        return "".join(st)


        
# @lc code=end

