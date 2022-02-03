'''
Given a number N, calculate the prime numbers up to N using Sieve of Eratosthenes.  

Example 1:

Input:
N = 10

Output:
2 3 5 7

Explanation:
Prime numbers less than equal to N 
are 2 3 5 and 7.
Example 2:

Input:
N = 35

Output:
2 3 5 7 11 13 17 19 23 29 31

Explanation:
Prime numbers less than equal to 35 are
2 3 5 7 11 13 17 19 23 29 and 31.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function sieveOfEratosthenes() which takes an integer N as an input parameter and return the list of prime numbers less than equal to N.

Expected Time Complexity: O(NloglogN)
Expected Auxiliary Space: O(N)

Constraints:
1<= N <= 104
'''
#User function Template for python3
import math
class Solution:
    def sieveOfEratosthenes(self, N):
    	#code here 
    	primes=[True]*(N+1)
        primes[0]=primes[1]=False
        for p in range(2,int(math.sqrt(N))+1):
            if primes[p]==True:
                for i in range(p*p,N+1,p):
                    primes[i]=False
        ans=[]
        for i in range(0,N+1):
            if primes[i]==True:
                ans.append(i)
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.sieveOfEratosthenes(N)
        for i in ans:
            print(i, end=" ")
        print()
# } Driver Code Ends
