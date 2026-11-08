class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        res=0
        num=0
        for i in d:
            if d[i]>res:
                res=d[i]
                num=i
        return num