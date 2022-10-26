"""
    Given two string A and B . Find the no of time B occur in A as a substring.
""" 

from itertools import count


class Solution():
    def countOccurrence(self,a,b):
        a = b+"@"+a
        
        z_array = [len(a)]
        rightBoxStart = 0
        rightBoxEnd = 0
        count = 0

        def doBruteForce():
            nonlocal rightBoxStart
            nonlocal rightBoxEnd
            nonlocal count

            while rightBoxEnd<len(a) and a[rightBoxEnd] == a[rightBoxEnd-rightBoxStart]:
                rightBoxEnd +=1

            length = rightBoxEnd - rightBoxStart
            if length == len(b):
                count +=1
            z_array.append(length)
            rightBoxEnd -= 1

        for i in range(1,len(a)):
            # when the i outside the box
            if i > rightBoxEnd:
                # do brute force
                rightBoxStart = i
                rightBoxEnd = i

                doBruteForce()
            # when the i inside the box
            else:
                # within the box
                j = i - rightBoxStart
                if z_array[j] < rightBoxEnd-i+1:
                    # just copy
                    z_array.append(z_array[j])
                else:
                    # set the box to current index
                    rightBoxStart = i
                    rightBoxEnd += 1

                    doBruteForce()

        return count

if __name__ == "__main__":
    test = Solution()
    print(test.countOccurrence("dhimanman","man"))

                

