class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        c=0
        prs=0
        d={0:1}
        for r in range(len(nums)):
            prs+=nums[r]
            if prs-k in d:
                c+=d[prs-k]
            d[prs]=d.get(prs,0)+1
        return c
