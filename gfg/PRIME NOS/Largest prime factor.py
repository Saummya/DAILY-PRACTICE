'''
Given a number N, the task is to find the largest prime factor of that number.
 

Example 1:

Input:
N = 5
Output:
5
Explanation:
5 has 1 prime factor 
i.e 5 only.
Example 2:

Input:
N = 24
Output:
3
Explanation:
24 has 2 prime factors 
3 and 2 in which 3 is 
greater

Your Task:
You don't need to read input or print anything. Your task is to complete the function largestPrimeFactor() which takes an integer N as input parameters and returns an integer, largest prime factor of N.
 

Expected Time Complexity: O(sqrt(N))
Expected Space Complexity: O(1)
 

Constraints:
1 <= N <= 105
'''
#User function Template for python3

class Solution:
    def largestPrimeFactor (self, N):
        # code here
        res = 1
        for i in range(2, N+1):
            while N%i==0:
                res = i
                N = N/i
            res = max(res, N)
        return res
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.largestPrimeFactor(N))
# } Driver Code Ends
