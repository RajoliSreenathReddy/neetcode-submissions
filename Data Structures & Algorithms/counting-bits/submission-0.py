class Solution:
    def countBits(self, n: int) -> List[int]:
        res=[]
        for i in range(n+1):
            bina=[]
            while i>0:
                bina.append(i%2)
                i//=2
            if bina:
                res.append(bina.count(1))
            else:
                res.append(0)
        return res