#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (33.76%)
# Likes:    29720
# Dislikes: 1263
# Total Accepted:    4M
# Total Submissions: 11.7M
# Testcase Example:  '"abcabcbb"'
#
# Given a string s, find the length of the longest substring without repeating
# characters.
# 
# 
# Example 1:
# 
# 
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# 
# 
# Example 2:
# 
# 
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# 
# 
# Example 3:
# 
# 
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a
# substring.
# 
# 
# 
# Constraints:
# 
# 
# 0 <= s.length <= 5 * 10^4
# s consists of English letters, digits, symbols and spaces.
# 
# 
#

# @lc code=start


class Solution:
    def noRepetition(self,s,mid):            
        for i in range(len(s)-mid+1):            
            if len(set(s[i:i+mid])) == mid:
                return True
        return False


    # Binary Search
    def lengthOfLongestSubstring1(self, s: str) -> int:        
        # define the search space
        lowerBound = 1 
        upperBound = len(s)
        ans = 0
        while lowerBound<=upperBound:
            mid = (lowerBound+upperBound)>>1
            if self.noRepetition(s,mid):
                ans = mid
                lowerBound = mid +1
            else:
                upperBound = mid -1
        return ans

    
    #two pointer
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = maxLength = 0
        usedChar ={}
        for i in range(len(s)):
            if s[i] in usedChar and start<=usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength,i-start+1)
            
            usedChar[s[i]] = i
        return maxLength




        
#@lc code=end

# if __name__ == "__main__":
#     test =Solution()
#     # print(test.lengthOfLongestSubstring("abcabcbb"))
#     # print(test.lengthOfLongestSubstring("bbbbb"))
#     # print(test.lengthOfLongestSubstring("pwwkew"))
#     print(test.lengthOfLongestSubstring("au"))