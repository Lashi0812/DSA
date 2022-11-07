# Design a class to find the kᵗʰ largest element in a stream. Note that it is 
# the kᵗʰ largest element in the sorted order, not the kᵗʰ distinct element. 
# 
#  Implement KthLargest class: 
# 
#  
#  KthLargest(int k, int[] nums) Initializes the object with the integer k and 
# the stream of integers nums. 
#  int add(int val) Appends the integer val to the stream and returns the 
# element representing the kᵗʰ largest element in the stream. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input
# ["KthLargest", "add", "add", "add", "add", "add"]
# [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
# Output
# [null, 4, 5, 5, 8, 8]
# 
# Explanation
# KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
# kthLargest.add(3);   // return 4
# kthLargest.add(5);   // return 5
# kthLargest.add(10);  // return 5
# kthLargest.add(9);   // return 8
# kthLargest.add(4);   // return 8
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= k <= 10⁴ 
#  0 <= nums.length <= 10⁴ 
#  -10⁴ <= nums[i] <= 10⁴ 
#  -10⁴ <= val <= 10⁴ 
#  At most 10⁴ calls will be made to add. 
#  It is guaranteed that there will be at least k elements in the array when 
# you search for the kᵗʰ element. 
#  
# 
#  Related Topics Tree Design Binary Search Tree Heap (Priority Queue) Binary 
# Tree Data Stream 👍 3597 👎 2113


# leetcode submit region begin(Prohibit modification and deletion)
from heapq import heappop, heappush, heapreplace


class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.min_heap = []
        for ele in nums:
            if len(self.min_heap) < self.k:
                heappush(self.min_heap, ele)
            else:
                if self.min_heap[0] < ele:
                    heapreplace(self.min_heap, ele)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.min_heap) < self.k:
            heappush(self.min_heap, val)
        elif self.min_heap[0] < val:
            heapreplace(self.min_heap, val)
        return self.min_heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# leetcode submit region end(Prohibit modification and deletion)
