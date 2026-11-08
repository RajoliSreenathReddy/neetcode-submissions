class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            c=0
            for j in range(len(nums)-i-1):
                if nums[j]>nums[j+1]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
                    c+=1
            if c==0:
                break
        return nums
                