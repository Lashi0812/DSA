#Given the integer array , find any pair (i,j) such that j > i and A[i] == A[j] and 
# (j-i) is minimium
import sys
class Solution():
    def findMinPair(self,array):
        hashmap = {}
        minDist = sys.maxsize
        for k,v in enumerate(array):
            if v in hashmap:
                minDist = min(minDist,k -hashmap[v] )
            hashmap[v] = k
        return minDist

if __name__ == "__main__":
    test = Solution()
    print(test.findMinPair([1,2,3,6,1,2,3,2,1]))