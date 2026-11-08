class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        d=dict(sorted(d.items(),key=lambda x:x[1],reverse=True))
        l=[]
        c=0
        for i in d:
            if c==k:
                break
            l.append(i)
            c+=1
        return l