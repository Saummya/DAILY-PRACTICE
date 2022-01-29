'''
Given a number N, you need to write a program that finds the sum of digits of the number till the number becomes a single digit and then check whether the number is Prime/Non-Prime.

Example 1:

Input:
N=5602
Output:
0
Explanation:
1st step=5+6+0+2=13
2nd step=1+3=4
Since 4 is not prime, so answer is 0.

Example 2:

Input:
N=12
Output:
1
Explanation:
1st step=1+2=3
Since, 3 is prime, so answer =1.

Your Task:
You don't need to read input or print anything.Your Task is to complete the function digitPrime() which takes a number N as input parameter and returns 1 if the final digit sum(adding digits until it becomes single-digit number) is prime.Otherwise, it returns 0.


Expected Time Complexity:O(1)
Expected Auxillary Space:O(1)


Constraints:
1<=N<=109
'''
#User function template for Python
import math
class Solution:
    def digitsPrime(self,N):
        #code here
        while True:
            sum1=0
            while(N):
                sum1+=N%10
                N=N//10
                
            N=sum1
            if sum1-9<=0:
                break
        return isprime(N)
  

  
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
#Initial template for Python

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        ob=Solution()
        print(ob.digitsPrime(N))
# } Driver Code Ends
