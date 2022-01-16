class Solution:
    def jump(self, nums: List[int]) -> int:
        i=len(nums)-1
        j=0
        count=0
        while i > 0 :
            while j < i:
                if i <= j+nums[j]:
                    #print(i,j)
                    i=j
                    j=0
                    count+=1
                    break
                else:
                    j+=1
            #return False
        return(count)
