class Solution:
    def isPalindrome(self, x: int) -> bool:
        i=0
        if x<0 or (x%10==0 and x!=0):
            return False
        while i<x:
            i=x%10+i*10
            x=int(x/10)
        return x==i or x==int(i/10)
        ## if its useless

a=Solution()
print(a.isPalindrome(13))