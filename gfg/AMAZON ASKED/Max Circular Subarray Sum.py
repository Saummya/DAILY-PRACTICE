'''
Given an array arr[] of N integers arranged in a circular fashion. Your task is to find the maximum contiguous subarray sum.


Example 1:

Input:
N = 7
arr[] = {8,-8,9,-9,10,-11,12}
Output:
22
Explanation:
Starting from the last element
of the array, i.e, 12, and 
moving in a circular fashion, we 
have max subarray as 12, 8, -8, 9, 
-9, 10, which gives maximum sum 
as 22.
Example 2:

Input:
N = 8
arr[] = {10,-3,-4,7,6,5,-4,-1}
Output:
23
Explanation: Sum of the circular 
subarray with maximum sum is 23

Your Task:
The task is to complete the function circularSubarraySum() which returns a sum of the circular subarray with maximum sum.


Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).


Constraints:
1 <= N <= 106
-106 <= Arr[i] <= 106
'''
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
