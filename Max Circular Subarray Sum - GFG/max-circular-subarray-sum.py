#User function Template for python3
import sys
#Complete this function
#Function to find maximum circular subarray sum.
def circularSubarraySum(arr,n):
    ##Your code here
    '''
    result=sys.maxint
    r= sys.minint
    s1=0
    s2=0
    s3=0
    for i in range(n):
        s1+=arr[i]
        s2+=arr[i]
        s3+=arr[i]
        s3=max(s3,arr[i])
        r=max(r,s3)
        s1=min(s1,arr[i])
        result=min(result,s1)
        
    if r<0:
        return r
    return max(s2-result,r)
    '''
    curr_max = arr[0]
    max_sum = arr[0]
    
    curr_min = arr[0]
    min_sum = arr[0]
    total_sum = sum(arr)
    
    for i in range(1, n):
        curr_max = max(curr_max+arr[i], arr[i])
        max_sum = max(curr_max, max_sum)
        
        curr_min = min(curr_min+arr[i], arr[i])
        min_sum = min(curr_min, min_sum)

    if min_sum == total_sum:
        return max_sum
    
    return max(max_sum, total_sum-min_sum)

#{ 
#  Driver Code Starts
#Initial Template for Python 3


import math
import sys

    
    

if __name__ == "__main__":
    T=int(input())
    while(T>0):
            
        n=int(input())
        
        arr=[int(x) for x in input().strip().split()]
            
        print(circularSubarraySum(arr,n))
        
        T-=1
    
# } Driver Code Ends