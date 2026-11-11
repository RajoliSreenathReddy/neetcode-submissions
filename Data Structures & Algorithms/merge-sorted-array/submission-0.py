class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        list1=[]
        for i in range(m):
            list1.append(nums1[i])
        for i in range(n):
            list1.append(nums2[i])
        list1.sort()
        for i in range(len(nums1)):
            nums1[i]=list1[i]