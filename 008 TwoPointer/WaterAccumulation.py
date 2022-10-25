# Given N array element where eac element are the height of the walls.
# Pick any 2 wall such that maximum ater is acculumated between the wall.




class Solution():
    def maxWaterAcc(self,array):
        i = 0
        j = len(array)-1
        ans = 0
        index = []
        while i<=j:
            water = (j-i) * min(array[j],array[i])
            if ans < water:
                ans = water
                index = [i,j]

            if array[i]>array[j]:
                j -= 1
            else:
                i +=1
        return index

if __name__ =="__main__":
    test = Solution()
    array = [3,5,4,7,3,6,5,4,1,2]
    print(test.maxWaterAcc(array))
