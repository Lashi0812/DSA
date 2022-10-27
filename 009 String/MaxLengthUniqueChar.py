"""
    Find the length of the longest substring which contains all unique / distinct character.
"""

class Solution():
    def maxLength(self,s:str):
        l = 0 
        r = 0
        #  Store the previous occurrence
        hashmap = {}
        maxLength = 0
        while r<len(s):
            if s[r] in hashmap:
                l = hashmap[s[r]] + 1
            hashmap[s[r]] = r
            maxLength = max(maxLength,r-l+1)
            r +=1
        return maxLength

if __name__ == "__main__":
    test = Solution()
    print(test.maxLength("aebcabgeb@#gbkdb#"))
                