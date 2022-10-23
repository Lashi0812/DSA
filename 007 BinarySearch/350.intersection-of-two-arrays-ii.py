#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#
# https://leetcode.com/problems/intersection-of-two-arrays-ii/description/
#
# algorithms
# Easy (55.53%)
# Likes:    5490
# Dislikes: 788
# Total Accepted:    933.3K
# Total Submissions: 1.7M
# Testcase Example:  '[1,2,2,1]\n[2,2]'
#
# Given two integer arrays nums1 and nums2, return an array of their
# intersection. Each element in the result must appear as many times as it
# shows in both arrays and you may return the result in any order.
# 
# 
# Example 1:
# 
# 
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# 
# 
# Example 2:
# 
# 
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000
# 
# 
# 
# Follow up:
# 
# 
# What if the given array is already sorted? How would you optimize your
# algorithm?
# What if nums1's size is small compared to nums2's size? Which algorithm is
# better?
# What if elements of nums2 are stored on disk, and the memory is limited such
# that you cannot load all elements into the memory at once?
# 
# 
#

# @lc code=start



from typing import List
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        hash_map = {}
        # insert array in the hash map
        for i in nums1:
            if i in hash_map:
                hash_map[i] = hash_map[i] + 1
            else:
                hash_map[i] = 1
        # find num in the hash map
        for j in nums2:
            if j in hash_map:
                res.append(j)
                hash_map[j] = hash_map[j]-1
                if hash_map[j] == 0:
                    hash_map.pop(j)
        return res

if __name__ == "__main__":
    test = Solution()
    print(test.intersect([1,2,2,1],[2,2]))
    print(test.intersect([4,9,5],[9,4,9,8,4]))


        
# @lc code=end

