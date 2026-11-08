class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[k]=nums[i]
                k+=1
        return k
        # i=0
        # while i<len(nums):
        #     if nums[i]==val:
        #         nums.remove(nums[i])
        #     else:
        #         i+=1
        # return len(nums)