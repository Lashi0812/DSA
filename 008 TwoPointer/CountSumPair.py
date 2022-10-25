# Given the sorted array with distinct element count the all the pair such that sums equal to k [i is not equal to j]


class Solution():
    # Brute Forece Apporach
    def bfa(self,array,target):
        count = 0 
        for i in range(len(array)-2):
            for j in range(i,len(array)-1):
                if array[i] + array[j] == target:
                    count += 1
        return count

    # Binary Search 
    def binarySearch(self,array,target):
        count = 0
        for i in range(len(array)-1):
            search = target - array[i]            
            lowerBound = i
            upperBound = len(array)-1
            while lowerBound<=upperBound:
                mid = (lowerBound +upperBound)>>1
                if array[mid]==search:
                    count += 1
                    break
                elif array[mid] > search:
                    upperBound = mid -1
                else:
                    lowerBound = mid + 1
        return count    

    # Two pointers
    def twoPointer(self,array,target):
        low = 0
        high = len(array)-1
        count = 0 
        while low<high:
            sums = array[low] +  array[high]
            if sums == target:
                # handle the duplicate

                # For the same element that form the target
                if (array[low] == array[high]):
                    cnt = high - low +1
                    # print("comb",cnt)
                    count = count + ((cnt * (cnt-1))>>1)
                    low = high +1
                    high = high+2

                # For the different element that form the target 
                else:
                    cnt1 = 0 
                    x = array[low]
                    # left side
                    while(low<high and x == array[low]):
                        cnt1 +=1
                        low +=1
                    # right side
                    cnt2 = 0
                    x = array[high]
                    while(low<high and x == array[high] ):
                        cnt2 +=1
                        high -=1
                    
                    # print("count",cnt1,cnt2)
                    count = count + (cnt1 * cnt2)


            elif sums > target:
                high -= 1
            else:
                low += 1
        return count 



    

if __name__ == "__main__":
    test = Solution()
    array1 = [-3,0,1,3,6,8,11,14,18,25]
    array2 = [1,3,4,5,6,7,10]
    array3 = [1,3,4,4,5,6,7,10]
    array4 = [1,3,4,4,5,6,6,6,7,10]
    array5 = [1,3,4,4,5,5,5,5,6,6,6,7,10]
    # print(test.bfa(array1,17))
    # print(test.binarySearch(array1,17))
    print(test.twoPointer(array1,17))
    print(test.twoPointer(array2,10))
    print(test.twoPointer(array3,10))
    print(test.twoPointer(array4,10))
    print(test.twoPointer(array5,10))
    print(test.twoPointer(array5,12))
