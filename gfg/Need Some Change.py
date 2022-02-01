'''
Given an array arr of n positive integers. The task is to swap every ith element of the array with (i+2)th element.

Note: When passing array to function, we basically pass the reference to the array. More details here. We'll learn more about pointers and references in upcoming module.

Example:

Input:
n = 5
arr[] = 1 2 3 4 5
Output:
3 4 5 2 1
Explanation:
Swapping 1 and 3, makes the array 3 2 1 4 5.
Now, swapping 2 and 4, makes the array 
3 4 1 2 5. Again,swapping 1 and 5, makes the 
array 3 4 5 2 1.
Your Task:
Your task is to complete the function swapElements(), which should swap each ith element with (i+2)th element. No need to print or return the array.
 

Expected Time Complexity: O(n)
Expected Auxilary Space: O(1)

Constraints:
1 <= N <= 106
1 <= Ai <= 106
'''

#User function Template for python3

class Solution:
	def swapElements(self, arr, n):
		#Code here
		for i in range(n-2):
		    arr[i],arr[i+2]=arr[i+2],arr[i]
		    
		return arr

#{ 
#  Driver Code Starts
#Initial Template for Python 3
		
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n = int(input())
        arr = list(map(int, input().strip().split()))
    	obj = Solution()
    	obj.swapElements(arr, n);
    	for i in arr:
    	    print(i, end = " ")
    	print()
# } Driver Code Ends
