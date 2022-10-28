#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#
# https://leetcode.com/problems/valid-anagram/description/
#
# algorithms
# Easy (62.69%)
# Likes:    7303
# Dislikes: 244
# Total Accepted:    1.8M
# Total Submissions: 2.8M
# Testcase Example:  '"anagram"\n"nagaram"'
#
# Given two strings s and t, return true if t is an anagram of s, and false
# otherwise.
# 
# An Anagram is a word or phrase formed by rearranging the letters of a
# different word or phrase, typically using all the original letters exactly
# once.
# 
# 
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
# Input: s = "rat", t = "car"
# Output: false
# 
# 
# Constraints:
# 
# 
# 1 <= s.length, t.length <= 5 * 10^4
# s and t consist of lowercase English letters.
# 
# 
# 
# Follow up: What if the inputs contain Unicode characters? How would you adapt
# your solution to such a case?
# 
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        need = len(t)
        hashmap = {}
        for ele in s:
            hashmap[ele] = hashmap.get(ele,0) + 1
        
        for ele in t:
            if ele in hashmap:
                hashmap[ele] -=1
                if hashmap[ele] >= 0:
                    need -=1
            else:
                return False
        
        if not need:
            return True
        else: return False

        
# @lc code=end

if __name__ == "__main__":
    test =Solution()
    print(test.isAnagram("anagram","nagaram"))
    print(test.isAnagram("rat","car"))

