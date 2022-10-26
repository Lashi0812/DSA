# Given an integer array . Find the longest subaaray with sum = 0

class Solution():
    def longestSubarray(self,array):
        hashmap = {}
        longest = 0
        prefix = 0 
        for k,v in enumerate(array):
            prefix += v
            if prefix in hashmap:
                longest = max(longest,k-hashmap[prefix])
            hashmap[prefix] = k
        return longest

if __name__ == "__main__":
    test = Solution()
    print(test.longestSubarray([2,2,1,-3,4,3,1,-8,6,-2,-1]))
