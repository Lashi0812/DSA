# Given the poistive element array ,Count the subarray that sum equals to k

from array import array
from cgitb import small
from genericpath import samefile
from itertools import count


class Solution():
    def prefix(self,array,target):
        # Time Complexlity  = O(n)
        # Space Complexlity = O(n) due to prefix sum array
        prefix_array = [0]
        count = 0
        # Compute the prefix array
        for k,v in enumerate(array):
            if prefix_array[k] == target:
                count +=1
            prefix_array.append(prefix_array[k]+v)
        # two pointer approach to find the diff 
        print(prefix_array,count)
        smaller = 0
        greater = 1
        while greater<len(prefix_array):
            diff = prefix_array[greater] - prefix_array[smaller]
            if diff == target:
                count +=1
                smaller +=1
                
            elif diff > target:
                smaller +=1
                if smaller == greater:
                    greater +=1
            else:
                greater += 1

        return count



        
         
if __name__ == "__main__":
    test = Solution()
    array = [3,2,5,0,1,8,6,2,10]
    print(test.prefix(array,15))


