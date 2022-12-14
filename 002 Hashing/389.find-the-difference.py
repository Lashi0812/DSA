#
# @lc app=leetcode id=389 lang=python3
#
# [389] Find the Difference
#
# https://leetcode.com/problems/find-the-difference/description/
#
# algorithms
# Easy (60.37%)
# Likes:    3308
# Dislikes: 399
# Total Accepted:    445.3K
# Total Submissions: 737.7K
# Testcase Example:  '"abcd"\n"abcde"'
#
# You are given two strings s and t.
# 
# String t is generated by random shuffling string s and then add one more
# letter at a random position.
# 
# Return the letter that was added to t.
# 
# 
# Example 1:
# 
# 
# Input: s = "abcd", t = "abcde"
# Output: "e"
# Explanation: 'e' is the letter that was added.
# 
# 
# Example 2:
# 
# 
# Input: s = "", t = "y"
# Output: "y"
# 
# 
# 
# Constraints:
# 
# 
# 0 <= s.length <= 1000
# t.length == s.length + 1
# s and t consist of lowercase English letters.
# 
# 
#

# @lc code=start
class Solution:

    # Using the Hashmap
    def findTheDifference1(self, s: str, t: str):
        hashmap = {}
        #build the hash map
        for ele in s:
            hashmap[ele] = hashmap.get(ele,0) + 1
        # search in the hash map
        for ele in t:
            if ele in hashmap:
                if hashmap[ele] == 0 :
                    return ele
                hashmap[ele] -= 1
            else:
                return ele

    def findTheDifference(self, s: str, t: str):
        c = 0
        for ele in s : c ^= ord(ele)
        for ele in t : c ^= ord(ele)
        return chr(c)

       
        
# @lc code=end

if __name__ == "__main__":
    test = Solution()
    print(test.findTheDifference1("abcd","abcde"))
    print(test.findTheDifference1("","y"))
    print(test.findTheDifference1("a","aa"))

    print(test.findTheDifference("abcd","abcde"))
    print(test.findTheDifference("","y"))
    print(test.findTheDifference("a","aa"))

