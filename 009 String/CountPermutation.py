"""
    Count all permutation of A in B as a substring
"""

class Solution():
    def countPermutation(self,A:str,B:str):
        count = 0
        # number of element needed 
        need = len(A)
        # what element are needed
        hashmap = {}
        for ele in A:
            if ele in hashmap:
                hashmap[ele] += 1
            else:
                hashmap[ele] = 1

        # first window
        for i in range(0,len(A)):
            if B[i] in hashmap:
                hashmap[B[i]] -=1
                if hashmap[B[i]] >= 0:
                    # we had what actually we wanted so decrease the need
                    need -=1

        # there is no need of element to form A then increase the count       
        if not need:
            count +=1
            
            

        for i in range(len(A),len(B)):
            # for the out going element of window
            if B[i-len(A)] in hashmap:
                hashmap[B[i-len(A)]] += 1
                if hashmap[B[i-len(A)]] > 0:
                    # we need this element but this element going out , so increase of need
                    need += 1
            
            # for the incoming element to window
            if B[i] in hashmap:
                hashmap[B[i]] -=1
                if hashmap[B[i]] >= 0:
                    # we had what actually we wanted so decrease the need
                    need -=1
            
            if not need:
                count += 1

        return count

if __name__ == "__main__":
    test = Solution()
    print(test.countPermutation("abc","abcbaccabc"))
    print(test.countPermutation("aca","acaa"))
    print(test.countPermutation("aabc","aebaca"))

            





