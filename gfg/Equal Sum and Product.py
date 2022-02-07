'''
Given an array Arr of length N, return the count of number of contiguous subarrays for which the sum and product of elements are equal.

Example 1:

Input:
N = 5
Arr[] = {1, 2, 3, 4, 5}
Output: 6
Explanation: All 6 subarrays having sum of
elements  equals to the product of
elements are: {1}, {2}, {3}, {4}, {5},
{1, 2, 3}
Your Task:
Complete the function numOfsubarrays() which takes an array arr, an integer n, as input parameters and returns an integer denoting the answer. You don't to print answer or take inputs.

Expected Time Complexity: O(N2)
Expected Auxiliary Space: O(1)

Constraints:
1 <= N <= 10
1 <= Arr[i] <= 10 where 1 <= i <= N
'''
import numpy as np
class Solution:

	
	def numOfsubarrays(self,arr, n):
    	# code here
    	#METHOD 1
    	'''
    	res=n
    	for i in range(n):
    	    s1=arr[i]
    	    p1=arr[i]
    	    #if s1==p1:
    	        #res+=1
    	    j=i+1
    	    while j<n:
    	        s1+=arr[i]
    	        p1*=arr[i]
    	        if s1==p1:
    	            res+=1
    	            j+=1
    	return res'''
    	
    	count=0
        for i in range(n-1):
            for j in range(i+1,n):
                if np.product(arr[i:j+1])==np.sum(arr[i:j+1]):
                    count+=1
        
        return count+n
