'''
Given N find all Sophie Germain Prime numbers less than N . A prime number p is called a sophie prime number if 2p+1 is also a prime number. The number 2p+1 is called a safe prime. 

Example 1:

Input: N = 5
Output: 2 3
Explanation: 2 and 3 are prime no. and 
2*2+1 = 5 and 3*2+1 = 7 are also prime
no.
Example 2:

Input: N = 3
Output: 2
Explanation: 2 is prime number and 2*2+1
= 5 is also a prime number.
 

Your Task:
You don't need to read or print anything your task is to complete the function sophie_primes() which takes N as input parameter and returns a list of all Sophie Germain Prime numbers in increasing order.
 

Expected Time Compelxity: O(N* log(N))
Expected Space Compelxity: O(N)

Constraints:
1 <= N <= 10000  
'''
#User function Template for python3
import math
class Solution:
	def sophie_Primes(self, n):
		# Code here
		l=[]
		for i in range(n):
		    if isprime(i)==1:
		        j=2*i+1
		        if isprime(j)==1:
		            l.append(i)
		return l
		    
		
def isprime(n):
    if n==1 or n==0:
        return 0
    if n==2 or n==3:
        return 1
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return 0
    return 1

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n= int(input())
		ob = Solution()
		ans = ob.sophie_Primes(n)
		for _ in ans:
			print(_, end = " ")
		print()
# } Driver Code Ends
