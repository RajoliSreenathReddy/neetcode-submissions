class Solution:
    def reverse(self, x: int) -> int:
        k=-1 if x<0 else 1
        
        m=0
        x=abs(x)
        while x>0:
            r=x%10
            m=m*10+r
            x=x//10
        m=m*k
        if m<-2**31 or m>2**31-1:
            return 0

        return m
        