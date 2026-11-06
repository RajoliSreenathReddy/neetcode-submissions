class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        l=[]
        for i in range(len(nums)):
            k=target-nums[i]
            if k in d:
                l.append(d[k])
                l.append(i)
            else:
                d[nums[i]]=i 
        return l 