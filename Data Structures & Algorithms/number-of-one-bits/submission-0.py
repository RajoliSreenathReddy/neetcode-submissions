class Solution:
    def hammingWeight(self, n: int) -> int:
        bina=[]
        while n>0:
            r=n%2
            bina.append(r)
            n//=2
        return bina.count(1)