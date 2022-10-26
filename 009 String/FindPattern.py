"""
Given the String S and a pattern T . Find if the there exists a substring in S which match the pattern T
"""


class Solution():
    def isPatternExist(self,s,t):
        s = t+"@"+s
        print(s)
               
        z_array = [len(s)]
        rightBoxStart = 0
        rightBoxEnd = 0

        def doBruteForce():
            
            nonlocal rightBoxEnd
            nonlocal rightBoxStart
            
            while rightBoxEnd<len(s) and s[rightBoxEnd]==s[rightBoxEnd-rightBoxStart]:
                rightBoxEnd +=1

            length = rightBoxEnd-rightBoxStart
            z_array.append(length)  
            rightBoxEnd -=1   

            return length
        

        # Construct the Z Array
        for i in range(1,len(s)):
            # when the i is outside the box
            if i > rightBoxEnd:
                rightBoxEnd   = i
                rightBoxStart = i
                # do brute force to find the prefix in the string
                if doBruteForce() == len(t):
                    print(z_array)
                    return True

            # when the i is inside the box    
            else:
                # within the box
                j = i - rightBoxStart
                if z_array[j] < rightBoxEnd-i+1:
                    # just copy
                    z_array.append(z_array[j])
                # touch the boundary or step over the boundary    
                else:
                    rightBoxStart = i
                    # shifting to calculated end
                    rightBoxEnd += 1
                    doBruteForce()
        print(z_array)
        return False

if __name__ == "__main__":
    test = Solution()
    print(test.isPatternExist("mynameissomething","iss"))
            

                
                