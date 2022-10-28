#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#
# https://leetcode.com/problems/group-anagrams/description/
#
# algorithms
# Medium (65.91%)
# Likes:    12224
# Dislikes: 378
# Total Accepted:    1.7M
# Total Submissions: 2.5M
# Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
#
# Given an array of strings strs, group the anagrams together. You can return
# the answer in any order.
# 
# An Anagram is a word or phrase formed by rearranging the letters of a
# different word or phrase, typically using all the original letters exactly
# once.
# 
# 
# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:
# Input: strs = [""]
# Output: [[""]]
# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]
# 
# 
# Constraints:
# 
# 
# 1 <= strs.length <= 10^4
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.
# 
# 
#
from typing import List
# @lc code=start
class Solution:

    # Using the Hashmap via sorted ele
    def groupAnagrams1(self, strs: List[str]) :
        hashmap = {}
        for ele in strs:
            sort_ele = "".join(sorted(ele))
            # print(sort_ele,hashmap)
            
            if sort_ele in hashmap:
                hashmap[sort_ele].append(ele)
            else:
                hashmap[sort_ele] = [ele]

        return list(hashmap.values())

    # Using hashmap via frequency array
    def groupAnagrams(self, strs: List[str]):
        hashmap = {}
        for word in strs:
            freq_array = [0]*26
            for ele in word:
                freq_array[ord(ele) - ord("a")] += 1

            if tuple(freq_array) in hashmap:
                hashmap[tuple(freq_array)].append(word)
            else:
                hashmap[tuple(freq_array)] = [word]
                
        return list(hashmap.values())
            


        
# @lc code=end

if __name__ == "__main__":
    test = Solution()
    print(test.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
