class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        j=0
        while(len(nums)>i):
            if(nums[i]!=0):
                p=nums[i]
                nums[i]=0
                nums[j]=p
                j=j+1
            i=i+1
