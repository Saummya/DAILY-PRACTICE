'''
Given an array A[] of N elements. The task is to count number of even and odd elements in the array.

Example:

Input:
N = 5
A[] = 1 2 3 4 5
Output:
3 2
Explanation:
There are 3 odd elements (1, 3, 5)
and 2 even elements (2 and 4).
Your Task:
Your task is to complete the function countOddEven() which should print number of odd and number of even elements in a single line seperated by space.
Print a newline at the end of output.

Constraints:
1 <= N <= 106
1 <= Ai <= 106
'''
class Solution:
	def countOddEven(self, arr, n):
		#Code here
		ce=0
		co=0
		for i in range(n):
		    if arr[i]%2==0:
		        ce+=1
		    else:
		        co+=1
		        
		print(co,ce)
