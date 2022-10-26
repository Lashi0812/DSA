# Given a string S , for every index i find the length of the longest substring from it which is equal to prefix of whole string

class Solution():
    def bruteForce(self,s):
        z_array = [len(s)]  
        for i in range(1,len(s)):
            j = i 
            while j<len(s) and s[j]==s[j-i]:
                j+=1
            z_array.append(j-i)
        return z_array

    def zAlgo(self,s):
       
        rightBoxStart = 0
        rightBoxEnd   = 0
        z_array = [len(s)]

        for i in range(1,len(s)):   
                        
            # When we are out of the Box
            if  i > rightBoxEnd: 
                rightBoxStart = i
                rightBoxEnd   = i

                # print("Applying the brute for ",i)
                
                # brute force
                while rightBoxEnd<len(s) and s[rightBoxEnd]==s[rightBoxEnd-rightBoxStart]:
                    rightBoxEnd+=1             
                
                z_array.append(rightBoxEnd-rightBoxStart)
                # update the box
                rightBoxEnd -= 1

            # when we are inside the box
            else:
                j = i - rightBoxStart
                if z_array[j] < rightBoxEnd-i+1:
                    # print("Copying the element for ",i)
                    # just copy
                    z_array.append(z_array[j])
                else:
                    rightBoxStart = i
                    rightBoxEnd +=1
                    while rightBoxEnd<len(s) and s[rightBoxEnd] == s[rightBoxEnd-rightBoxStart]:
                        rightBoxEnd+=1 
                      
                    z_array.append(rightBoxEnd-rightBoxStart)

                    # update the box                    
                    rightBoxEnd -= 1


        return z_array

            




if __name__ == "__main__":
    test = Solution()
    s = "xxyzxxyzwxxyzxxyzx"
    s1 = "xxyxxyxxaxxyxxz"
    # print(test.bruteForce(s))
    # print(test.zAlgo(s))
    print(test.bruteForce(s1))
    print(test.zAlgo(s1))
    print(test.zAlgo("slak@mynameislakshman"))
        