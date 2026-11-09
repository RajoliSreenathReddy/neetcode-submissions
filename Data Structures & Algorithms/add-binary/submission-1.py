class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def dec(n):
            dec=0
            c=0
            for i in range(len(n)-1,-1,-1):
                num=int(n[i])
                dec+=num*(2**c)
                c+=1
            return dec
        if a=="0" and b=="0":
            return "0"
        x=dec(a)
        y=dec(b)
        res=x+y
        bina=[]
        while res>0:
            bina.append(str(res%2))
            res//=2
        return "".join(bina[::-1])
