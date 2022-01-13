class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        #using two pointer concept
        left=0
        right=len(nums)-1
        ans=[0]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            if abs(nums[left])>abs(nums[right]):
                ans[i]=nums[left]**2
                left+=1
                
            else:
                ans[i]=nums[right]**2
                right-=1
                
        return ans
