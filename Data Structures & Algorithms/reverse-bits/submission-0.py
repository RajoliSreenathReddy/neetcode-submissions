class Solution:
    def reverseBits(self, n: int) -> int:
        bina=[]
        while n>0:
            bina.append(str(n%2))
            n//=2
        while len(bina)<32:
            bina.append("0")
        s=bina
        dec=0
        c=0
        for i in range(len(s)-1,-1,-1):
            dec+=int(s[i])*(2**c)
            c+=1
        return dec