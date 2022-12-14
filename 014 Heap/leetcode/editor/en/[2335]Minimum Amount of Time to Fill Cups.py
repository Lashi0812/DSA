# You have a water dispenser that can dispense cold, warm, and hot water. Every 
# second, you can either fill up 2 cups with different types of water, or 1 cup 
# of any type of water. 
# 
#  You are given a 0-indexed integer array amt of length 3 where amt[0],
# amt[1], and amt[2] denote the number of cold, warm, and hot water cups you
# need to fill respectively. Return the minimum number of seconds needed to fill 
# up all the cups. 
# 
#  
#  Example 1: 
# 
#  
# Input: amt = [1,4,2]
# Output: 4
# Explanation: One way to fill up the cups is:
# Second 1: Fill up a cold cup and a warm cup.
# Second 2: Fill up a warm cup and a hot cup.
# Second 3: Fill up a warm cup and a hot cup.
# Second 4: Fill up a warm cup.
# It can be proven that 4 is the minimum number of seconds needed.
#  
# 
#  Example 2: 
# 
#  
# Input: amt = [5,4,4]
# Output: 7
# Explanation: One way to fill up the cups is:
# Second 1: Fill up a cold cup, and a hot cup.
# Second 2: Fill up a cold cup, and a warm cup.
# Second 3: Fill up a cold cup, and a warm cup.
# Second 4: Fill up a warm cup, and a hot cup.
# Second 5: Fill up a cold cup, and a hot cup.
# Second 6: Fill up a cold cup, and a warm cup.
# Second 7: Fill up a hot cup.
#  
# 
#  Example 3: 
# 
#  
# Input: amt = [5,0,0]
# Output: 5
# Explanation: Every second, we fill up a cold cup.
#  
# 
#  
#  Constraints: 
# 
#  
#  amt.length == 3
#  0 <= amt[i] <= 100
#  
# 
#  Related Topics Array Greedy Heap (Priority Queue) 👍 368 👎 52


# leetcode submit region begin(Prohibit modification and deletion)
import heapq


class Solution(object):
    def fillCups(self, amount):
        """
        :type amount: List[int]
        :rtype: int
        """
        return max(max(amount), (sum(amount) + 1) // 2)

        # leetcode submit region end(Prohibit modification and deletion)

# %%
