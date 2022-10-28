#
# @lc app=leetcode id=149 lang=python3
#
# [149] Max Points on a Line
#
# https://leetcode.com/problems/max-points-on-a-line/description/
#
# algorithms
# Hard (21.68%)
# Likes:    1607
# Dislikes: 246
# Total Accepted:    255.9K
# Total Submissions: 1.2M
# Testcase Example:  '[[1,1],[2,2],[3,3]]'
#
# Given an array of points where points[i] = [xi, yi] represents a point on the
# X-Y plane, return the maximum number of points that lie on the same straight
# line.
# 
# 
# Example 1:
# 
# 
# Input: points = [[1,1],[2,2],[3,3]]
# Output: 3
# 
# 
# Example 2:
# 
# 
# Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# Output: 4
# 
# 
# 
# Constraints:
# 
# 
# 1 <= points.length <= 300
# points[i].length == 2
# -10^4 <= xi, yi <= 10^4
# All the points are unique.
# 
# 
#
from itertools import count
from typing import List
# @lc code=start
class Solution:

    def countPoints(self,slope,intercept,points):
        count = 0
        for pt in points:
            
            if pt[1] == round(((slope * pt[0]) + intercept),5):
                count += 1
        return count

    def maxPoints(self, points: List[List[int]]) -> int:
        maxi = 0
        # compute slope and intercept of any two point 
        for i in range(len(points)):
            for j in range(i,len(points)):
                pt1 = points[i]
                pt2 = points[j]
                # for line not parallel to y axis
                if (pt2[0] - pt1[0]) != 0 :
                    slope = (pt2[1] - pt1[1]) / (pt2[0] - pt1[0])
                    intercept = pt1[1] - (slope * pt1[0])
                    # print(slope,intercept)
                    maxi = max(maxi,self.countPoints(slope,intercept,points))
                # for line parallel to y axis    
                else:
                    count = 0
                    for pt in points:
                        if pt[0] == pt1[0]:
                            count +=1
                    maxi = max(maxi,count)

        return maxi


# if __name__ == "__main__":
#     test =Solution()
#     print(test.maxPoints([[-6,-1],[3,1],[12,3]]))


        
# @lc code=end

