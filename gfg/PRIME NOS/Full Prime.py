'''
Given a number N.Check if it is Full Prime or not. 
Note : A full prime number is one in which the number itself is prime and all its digits are also prime.


Example 1:

Input:
N=31
Output:
0
Explanation:
N is prime but since 1 is not a 
prime so all the digits of N
are not prime.So, Answer is 0.

Example 2:

Input:
N=37
Output:
1
Explanation:
N is prime and so is all of its digits.
Thus, Answer is 1.

Your Task:
You don't need to read input or print anything.Your task is to complete the function fullPrime() which takes the number N as input parameter and returns 1 if the number is Full Prime.Otherwise return 0.


Expected Time Complexity:O(Sqrt(N))
Expected Auxillary Space:O(1)


Constraints:
1<=N<=109
'''
#User function Template for python3
import math
class Solution:
    def fullPrime(self,N):
        #code here
        flag = 0
        if N>1:
            for i in range(2,int(math.sqrt(N))+1):
                if N%i == 0:
                    return 0
            else:
                flag = 1
        
            if flag == 1:
                x = str(N)
                for i in x:
                    # print(i)
                    if int(i) <= 1:
                        return 0
                    else:
                        for j in range(2,int(math.sqrt(int(i)))+1):
                            if int(i)%j == 0:
                                return 0
            return 1
        else:
            return 0
        

        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        ob=Solution()
        print(ob.fullPrime(N))
# } Driver Code Ends
