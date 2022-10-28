#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#
# https://leetcode.com/problems/first-unique-character-in-a-string/description/
#
# algorithms
# Easy (58.83%)
# Likes:    6867
# Dislikes: 231
# Total Accepted:    1.3M
# Total Submissions: 2.2M
# Testcase Example:  '"leetcode"'
#
# Given a string s, find the first non-repeating character in it and return its
# index. If it does not exist, return -1.
# 
# 
# Example 1:
# Input: s = "leetcode"
# Output: 0
# Example 2:
# Input: s = "loveleetcode"
# Output: 2
# Example 3:
# Input: s = "aabb"
# Output: -1
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^5
# s consists of only lowercase English letters.
# 
# 
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = {}
        for ele in s:
            hashmap[ele] = hashmap.get(ele,0) + 1
        for idx,ele in enumerate(s):
            if hashmap[ele] == 1:
                return idx
        return -1
# @lc code=end

