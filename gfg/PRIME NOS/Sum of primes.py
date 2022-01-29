'''
Your task is to calculate sum  of primes present as digits of given number N.

Example 1:

Input: 333
Output: 9
Explaination: 3 is a prime number. It 
is present 3 times. So 3+3+3 = 9.
Example 2:

Input: 686
Output: 0
Explaination: Neither 6 nor 8 is a 
prime number.
Your Task:
You do not need to read input or print anything. Your task is to complete the function primeSum() which takes N as input parameter and returns the sum of all the prime digits present in the number N.

Expected Time Complexity: O(logN)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ N ≤ 5*104   


'''
#User function Template for python3
import math
class Solution:
    def primeSum(self, N):
        # code here
        sum = 0
        if N == 2: #smallest prime number
            return 2
        else:
            mstr = str(N)
           
            for n in mstr:
                n = int(n)
                if self.isPrimeNumber(n):
                    sum += n
        return sum
           
    def isPrimeNumber(self,num):
        if num < 2:
            return False
           
        for i in range(2,num):
            if num%i == 0:
                return False
        return True
      
   
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        print(ob.primeSum(N))
# } Driver Code Ends
