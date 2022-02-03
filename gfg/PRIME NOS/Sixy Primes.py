'''
Sixy primes are prime numbers that differ from each other by six. For example, the numbers 5 and 11 are both sixy primes, because they differ by 6. Given a range of the form [L, R]. The task is to find all the sixy prime pairs in the range in increasing order.

Example 1:

Input: L = 11, R = 19
Output: [11, 17, 13, 19] 
Explanation: There are total two pair possible
with difference 6 and these are 11,17,13,19.  

Example 2:

Input: L = 6, R = 20
Output: [7, 13, 11, 17, 13, 19]
Explanation: There are total three pair possible
with difference 6 and these are 7,13,11,17,13,19. 

Your Task:  
You dont need to read input or print anything. Complete the function sixyPrime() which takes L and R as input parameter and returns all the sixy prime exist and if there are no sixy prime exist returns -1.

Expected Time Complexity: O(nloglogn)
Expected Auxiliary Space: O(n)

Constraints:
1 <= L <= R <=103
'''
#User function Template for python3

import math
class Solution:
	def sixyPrime(self, L, R):
		# code here
		        
        primes = [True]*(R+1)
        p = 2
        while p*p<R+1:
            if primes[p]==True:
                for i in range(p*p, R+1, p):
                    primes[i] = False
            p+=1
        ans = []
        for i in range(L, R-5):
            if primes[i] == True and primes[i+6]==True:
                ans.append(i)
                ans.append(i+6)
        return ans if len(ans)>0 else [-1]
		
		
		


#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		L,R = input().split()
		L=int(L)
		R=int(R)
		ob = Solution();
		ans = ob.sixyPrime(L,R)
		for i in range(len(ans)):
			print(ans[i], end = " ")
		print()

# } Driver Code Ends
