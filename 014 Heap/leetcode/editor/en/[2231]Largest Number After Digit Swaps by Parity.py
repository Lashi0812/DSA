# You are given a positive integer num. You may swap any two digits of num that 
# have the same parity (i.e. both odd digits or both even digits). 
# 
#  Return the largest possible value of num after any number of swaps. 
# 
#  
#  Example 1: 
# 
#  
# Input: num = 1234
# Output: 3412
# Explanation: Swap the digit 3 with the digit 1, this results in the number 321
# 4.
# Swap the digit 2 with the digit 4, this results in the number 3412.
# Note that there may be other sequences of swaps but it can be shown that 3412 
# is the largest possible number.
# Also note that we may not swap the digit 4 with the digit 1 since they are of 
# different parities.
#  
# 
#  Example 2: 
# 
#  
# Input: num = 65875
# Output: 87655
# Explanation: Swap the digit 8 with the digit 6, this results in the number 856
# 75.
# Swap the first digit 5 with the digit 7, this results in the number 87655.
# Note that there may be other sequences of swaps but it can be shown that 87655
#  is the largest possible number.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= num <= 10⁹ 
#  
# 
#  Related Topics Sorting Heap (Priority Queue) 👍 346 👎 225


# leetcode submit region begin(Prohibit modification and deletion)
import heapq


class Solution(object):
    def largestInteger(self, num):
        """
        :type num: int
        :rtype: int
        """
        max_odd_heap = []
        max_even_heap = []
        for ele in str(num):
            ele = int(ele)
            if ele % 2 == 0:
                heapq.heappush(max_even_heap, -ele)
            else:
                heapq.heappush(max_odd_heap, -ele)

        ans = ""
        for ele in str(num):
            ele = int(ele)
            if ele % 2 == 0:
                ans += str(-heapq.heappop(max_even_heap))
            else:
                ans += str(-heapq.heappop(max_odd_heap))

        return int(ans)


# leetcode submit region end(Prohibit modification and deletion)
