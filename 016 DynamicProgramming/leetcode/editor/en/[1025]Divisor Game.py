# Alice and Bob take turns playing a game, with Alice starting first. 
# 
#  Initially, there is a number n on the chalkboard. On each player's turn, 
# that player makes a move consisting of: 
# 
#  
#  Choosing any x with 0 < x < n and n % x == 0. 
#  Replacing the number n on the chalkboard with n - x. 
#  
# 
#  Also, if a player cannot make a move, they lose the game. 
# 
#  Return true if and only if Alice wins the game, assuming both players play 
# optimally. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 2
# Output: true
# Explanation: Alice chooses 1, and Bob has no more moves.
#  
# 
#  Example 2: 
# 
#  
# Input: n = 3
# Output: false
# Explanation: Alice chooses 1, Bob chooses 1, and Alice has no more moves.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 1000 
#  
# 
#  Related Topics Math Dynamic Programming Brainteaser Game Theory 👍 1635 👎 35
# 18


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def divisorGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        store = [False] * (n + 1)
        for i in range(2, n + 1):
            for j in range(1, i):
                if i % j == 0 and not store[i]:
                    store[i] = not store[i-j]

        return store[-1]

# leetcode submit region end(Prohibit modification and deletion)
# %%
# store = [0, 0, float("inf"), float("inf"), float("inf"), float("inf"), float("inf")]
# for i in range(2, 7):
#     for j in range(1, i):
#         if i % j == 0:
#             print(f"i = {i} , seeing= {i - j} cur_max ={store[i]}")
#             store[i] = min(store[i - j], store[i])
#             print(f"changed {store[i]}")
#     store[i] += 1
# print(store)
