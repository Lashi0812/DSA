# Given an integer numRows, return the first numRows of Pascal's triangle. 
# 
#  In Pascal's triangle, each number is the sum of the two numbers directly 
# above it as shown: 
#  
#  
#  Example 1: 
#  Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
#  
#  Example 2: 
#  Input: numRows = 1
# Output: [[1]]
#  
#  
#  Constraints: 
# 
#  
#  1 <= numRows <= 30 
#  
# 
#  Related Topics Array Dynamic Programming 👍 8414 👎 277


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 1:
            return [[1]]

        final = [[1]]
        for row in range(1, numRows):
            temp = [1]
            for col in range(1, row):
                temp.append(final[row-1][col] + final[row-1][col - 1])
            temp.append(1)
            final.append(temp)

        return final



# leetcode submit region end(Prohibit modification and deletion)


# %%
# store = [1]
# for row in range(1, 10):
#     print(store)
#     temp = [1]
#     for col in range(1, row):
#         temp.append(store[col] + store[col - 1])
#     temp.append(1)
#     store = temp
