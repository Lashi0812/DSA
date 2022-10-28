#
# @lc app=leetcode id=500 lang=python3
#
# [500] Keyboard Row
#
# https://leetcode.com/problems/keyboard-row/description/
#
# algorithms
# Easy (69.03%)
# Likes:    1112
# Dislikes: 998
# Total Accepted:    168.2K
# Total Submissions: 243.5K
# Testcase Example:  '["Hello","Alaska","Dad","Peace"]'
#
# Given an array of strings words, return the words that can be typed using
# letters of the alphabet on only one row of American keyboard like the image
# below.
# 
# In the American keyboard:
# 
# 
# the first row consists of the characters "qwertyuiop",
# the second row consists of the characters "asdfghjkl", and
# the third row consists of the characters "zxcvbnm".
# 
# 
# 
# Example 1:
# 
# 
# Input: words = ["Hello","Alaska","Dad","Peace"]
# Output: ["Alaska","Dad"]
# 
# 
# Example 2:
# 
# 
# Input: words = ["omk"]
# Output: []
# 
# 
# Example 3:
# 
# 
# Input: words = ["adsdf","sfd"]
# Output: ["adsdf","sfd"]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= words.length <= 20
# 1 <= words[i].length <= 100
# words[i] consists of English letters (both lowercase and uppercase). 
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
                
        for word in words.copy():
            row = 0
            for ele in word:                
                if ele.lower() in "qwertyuiop" and (row== 0 or row==1 ):
                    row = 1
                elif ele.lower() in "asdfghjkl" and (row== 0 or row==2 ):
                    row = 2
                elif ele.lower() in "zxcvbnm" and (row== 0 or row==3 ):
                    row = 3
                else:
                    words.remove(word)
                    break
        return words

if __name__ == "__main__":
    test = Solution()
    print(test.findWords(["Hello","Alaska","Dad","Peace"]))
    print(test.findWords(["omk"]))
    print(test.findWords(["adsdf","sfd"]))
    print(test.findWords(["abdfs","cccd","a","qwwewm"]))
# @lc code=end

