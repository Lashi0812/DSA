# You are climbing a staircase. It takes n steps to reach the top. 
# 
#  Each time you can either climb 1 or 2 steps. In how many distinct ways can 
# you climb to the top? 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
#  
# 
#  Example 2: 
# 
#  
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 45 
#  
# 
#  Related Topics Math Dynamic Programming Memoization 👍 15299 👎 452


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    # def climbStairs(self, n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
    #     store = [None] * (n + 1)
    #
    #     def solve(x):
    #         # base condition
    #         if x == 0 or x == 1:
    #             return 1
    #         # check already solved
    #         if store[x] is not None:
    #             return store[x]
    #
    #         # solve and store the problem
    #         store[x] = solve(x - 1) + solve(x - 2)
    #
    #         return store[x]
    #
    #     return solve(n)
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = 1
        b = 1

        for _ in range(2, n + 1):
            a, b = b, a + b

        return b

# leetcode submit region end(Prohibit modification and deletion)
