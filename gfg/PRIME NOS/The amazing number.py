'''
You are given a number N. Your task is to determine if N is an amazing number or not.  A number is called amazing if it has exactly three distinct divisors.

Example 1:

Input: N = 3
Output: 0 
Explanation: 3 has only two divisors
1 and 3.So answer is 0.
Example 2:

Input: N = 4
Output: 1
Explanation: 4 has Exactly Three divisors
1, 2 and 4.So answer is 1. 


Your Task:  
You dont need to read input or print anything. Complete the function isAmazing() which takes N as input parameter and returns 1 if N is an amazing number else return 0.

Expected Time Complexity: O(N1/4)
Expected Auxiliary Space: O(1)

Constraints:
1<= N <=1018

'''
#User function Template for python3
import math
class Solution:
    def isAmazing (self, n):
        # code here 
        '''
        if the number is a perfect square and its sqrt is a prime number, 
        then it'll have only 3 factors
        '''
        if(n==4):
            return 1
            
        n=int(n**(1/2))
        if(n==1):
            return 0
        for i in range(2,n+1):
            if(n%i==0):
                return 0
        return 1
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        
        ob = Solution()
        print(ob.isAmazing(n))
# } Driver Code Ends
