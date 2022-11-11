# The Tribonacci sequence Tn is defined as follows: 
# 
#  T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0. 
# 
#  Given n, return the value of Tn. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 4
# Output: 4
# Explanation:
# T_3 = 0 + 1 + 1 = 2
# T_4 = 1 + 1 + 2 = 4
#  
# 
#  Example 2: 
# 
#  
# Input: n = 25
# Output: 1389537
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= n <= 37 
#  The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 -
#  1. 
#  
# 
#  Related Topics Math Dynamic Programming Memoization 👍 2402 👎 129


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        # if n == 0:
        #     return 0
        #
        # a = 0
        # b = 1
        # c = 1
        # for _ in range(2, n):
        #     a, b, c = b, c, a + b + c
        # return c

        store = {0: 0, 1: 1, 2: 1}
        for i in range(3, n + 1):
            store[i] = store[i - 1] + store[i - 2] + store[i - 3]
        return store[n]

# leetcode submit region end(Prohibit modification and deletion)
