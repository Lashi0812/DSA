# Given the sorted array with distinct element, count all th pair (i,j) such that diff is equal to k

class Solution():
    # two pointer
    def twoPointer(self,array,target):
        count = 0
        target = abs(target)
        smaller = 0
        greater = 1
        while greater < len(array):
            
            diff = array[greater] - array[smaller]
            if  diff== target:
                count   +=1
                smaller += 1
                greater += 1
            elif diff > target:
                # increase the smaller value 
                smaller +=1
                if smaller == greater:
                    greater +=1

            else:
                # increase the greater value
                greater +=1
        return count

if __name__ == "__main__":
    test = Solution()
    array1 = [-3,0,1,3,6,8,11,14,18,25]
    print(test.twoPointer(array1,5))

        
