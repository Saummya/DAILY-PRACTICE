#User function Template for python3

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
   
    def maxSubArraySum(self,arr,N):
        ##Your code here
        max_so_far= arr[0]
        max1=0
        for i in range(N):
            max1+=arr[i]
            max_so_far=max(max_so_far,max1)
            if max1<0:
                max1=0
            
        return max_so_far
            

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