#User function Template for python3

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        ##Your code here
        curr_sum=0
        max_so_far=arr[0]
        
        st=0
        en=0
        poi=0
        
        for i in range(0,N):
            curr_sum+=arr[i]
            
            if max_so_far<curr_sum:
                max_so_far=curr_sum
                st=poi
                en=i
                
            if curr_sum<0:
                curr_sum=0
                poi=i+1
                
        s=0
        for i in range(st,en+1):
            s=s+arr[i]
            
        return s
                

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

 
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            
            print(ob.maxSubArraySum(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends