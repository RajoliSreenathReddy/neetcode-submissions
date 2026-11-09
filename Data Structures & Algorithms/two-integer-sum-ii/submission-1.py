class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(numbers)):
            x=target-numbers[i]
            if x in d:
                return [d[x]+1,i+1]
            else:
                d[numbers[i]]=i