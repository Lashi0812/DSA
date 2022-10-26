# Given an array. Find the length of the largest sequence which can be rearranged to get consecutive element

class Solution():
    def largestSequence(self,array):
        # build the hash set
        hashset = set(array)
        largest = 0
        for v in array:
            if v-1 not in hashset:
                count = 1
                while v+1 in hashset:
                    count +=1
                    v += 1
                largest = max(largest,count)
        return largest

if __name__ == "__main__":
    test = Solution()
    print(test.largestSequence([100,4,3,6,10,20,11,5,101]))
    print(test.largestSequence([]))
    print(test.largestSequence([1,3,5,7,9]))
    print(test.largestSequence([-1,8,2,3,7,1,4,9]))
                
