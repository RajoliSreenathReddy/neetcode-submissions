class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        l=[]
        for i in d:
            if d[i]>n//3:
                l.append(i)
        return l
      