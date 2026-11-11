class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i=1
        while i<len(nums)+1:
            if i not in nums:
                return i
            i+=1
        else:
            return i