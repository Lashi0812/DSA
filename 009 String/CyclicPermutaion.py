"""
    Given a binary string B , Count all the cyclic permutation of the string such that B^cyclic permutation = 0
"""

class Solution():
    def countCyclic(self,b:str):
        string_length = len(b)
        b = b+"@"+b*2
        z_array = [len(b)]
        rightBoxStart = 0
        rightBoxEnd = 0
        count = 0

        def doBruteForce():
            nonlocal rightBoxEnd
            nonlocal count

            while rightBoxEnd<len(b) and b[rightBoxEnd]==b[rightBoxEnd-rightBoxStart]:
                rightBoxEnd += 1
            
            length = rightBoxEnd-rightBoxStart
            z_array.append(length)
            rightBoxEnd -=1

            if length == string_length:
                count +=1

            

        for i in range(1,len(b)):
            # when the i outside the box
            if i > rightBoxEnd:
                rightBoxStart = i
                rightBoxEnd = i 

                doBruteForce()

            else:
                j = i - rightBoxStart
                if z_array[j]<rightBoxEnd-i+1:
                    z_array.append(z_array[j])
                else:
                    rightBoxStart = i
                    rightBoxEnd += 1
                    doBruteForce()
        return count-1

if __name__ == "__main__":
    test = Solution()
    print(test.countCyclic("1010"))
