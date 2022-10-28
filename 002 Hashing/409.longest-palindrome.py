#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#
# https://leetcode.com/problems/longest-palindrome/description/
#
# algorithms
# Easy (54.61%)
# Likes:    3800
# Dislikes: 224
# Total Accepted:    401.9K
# Total Submissions: 736K
# Testcase Example:  '"abccccdd"'
#
# Given a string s which consists of lowercase or uppercase letters, return the
# length of the longest palindrome that can be built with those letters.
# 
# Letters are case sensitive, for example, "Aa" is not considered a palindrome
# here.
# 
# 
# Example 1:
# 
# 
# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose
# length is 7.
# 
# 
# Example 2:
# 
# 
# Input: s = "a"
# Output: 1
# Explanation: The longest palindrome that can be built is "a", whose length is
# 1.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 2000
# s consists of lowercase and/or uppercase English letters only.
# 
# 
#

# @lc code=start



class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq_array = [0]*128
        oddGroup = 0
        for ele in s:
            freq_array[ord(ele)] += 1
        for freq in freq_array: 
            oddGroup += freq & 1
        return len(s) - oddGroup + (oddGroup>0)

        


    def longestPalindrome1(self, s: str) -> int:
        hashmap = {}
        count = 0
        singleOdd = 0
        moreOdd = 0
        for ele in s:
            hashmap[ele] = hashmap.get(ele,0)+1
        for k,v in hashmap.items():
            #print(k,v)
            if v%2 == 0:
                count += v
            else:
                if v == 1:
                    singleOdd +=1
                else:
                    moreOdd += 1
                    count += v
        return count - moreOdd + (1 if moreOdd or singleOdd else 0)


if __name__ == "__main__":
    test = Solution()
    print(test.longestPalindrome("abccccdd"))
    print(test.longestPalindrome("aa"))
    print(test.longestPalindrome("aaacccbbbbbccccddAA"))




# @lc code=end

