'''
Given a number N. Check whether N is a Twisted Prime number or not.
Note: A number is called Twisted Prime if it is a prime and its reverse is also a prime.

Example 1:

Input: N = 97
Output: 1
Explanation: 97 is a prime number. Its 
reverse 79 isalso a prime number. Thus 
97 is a  twisted Prime and so, answer is 1.
Example 2:

Input: N = 43
Output: 0
Explanation: 43 is a prime number but its 
reverse 34 is not a prime.So, 43 is not a 
twisted prime and thus, answer is 0.

Your Task:You don't need to read input or print anything.Your task is to complete the function isTwistedPrime() which takes a number N as input parameter and returns 1 if it is a twisted prime number.Otherwise, it returns 0.


Expected Time Complexity:(O(sqrt(max(N,RevN))), here RevN is the reverse of N.
Expected Space Complexity:O(1)


Constraints:
1<=N<=109
'''
#User function Template for python3

class Solution:
    def isTwistedPrime(self,N):
        #code here
        if isprime(N)==1 and isprime(rev(N))==1:
            return 1
        else:
            return 0
   
        
def isprime(n):
    if n==1 or n==0:
        return 0
    if n==2 or n==3:
        return 1
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return 0
    return 1
    
def rev(n):
    n1=str(n)
    n1=n1[::-1]
    n2=int(n1)
    return n2

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        ob=Solution()
        print(ob.isTwistedPrime(N))
# } Driver Code Ends
