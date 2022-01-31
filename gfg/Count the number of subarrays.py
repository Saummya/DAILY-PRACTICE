'''
Given an array A[] of N integers and a range(L, R). The task is to find the number of subarrays having sum in the range L to R (inclusive).

Example 1:

Input:
N = 3, L = 3, R = 8
A[] = {1, 4, 6}
Output: 
3
Explanation: 
The subarrays are [1,4], [4] and [6]
Example 2:

Input:
N = 4, L = 4, R = 13
A[] = {2, 3, 5, 8}
Output: 
6
Explanation: 
The subarrays are [2,3], [2,3,5], 
[3,5],[5], [5,8] and [8]
Your Task: 
You don't need to read input or print anything. Complete the function countSubarray( ) which takes the integer N , the array A[], the integer L and the integer R as input parameters and returns the number of subarays. 

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ N ≤ 106
1 ≤ A[] ≤ 109
1 ≤ L ≤ R ≤ 1015
'''


#SOLUTION:

'''
We can solve this using sliding window and a key insight.

Getting the number of subarrays with sum in the range [L, R] using sliding window is difficult, but we can transform the problem into another easier one - Find number of subarrays with sum ≤ k.

How can we use that here?

Well, number of subarrays with sum in range [L, R] =  (number of subbarrays with the sum ≤ R) - (number of subarrays with sum ≤ L-1).

And that's it, the code then becomes pretty easy.
'''

#User function Template for python3
class Solution:
    def countSubarray(self, N, A, L, R):
        # code here
        '''
        We can solve this using sliding window and a key insight.

        Getting the number of subarrays with sum in the range [L, R] using sliding window is difficult,
        but we can transform the problem into another easier one - Find number of subarrays with sum ≤ k.
        How can we use that here?
        Well, number of subarrays with sum in range [L, R] =
        (number of subbarrays with the sum ≤ R) - (number of subarrays with sum ≤ L-1).
        And that's it, the code then becomes pretty easy.'''
        
        i=0
        sum1=0
        count1=0
        for j in range(N):
            sum1+=A[j]

            while i<=j and sum1>R:
                sum1-=A[i]
                i+=1
            count1+=(j-i+1)

        
        i=sum1=count2=0
        
        for j in range(N):
            sum1+=A[j]

            while i<=j and sum1>(L-1):
                sum1-=A[i]
                i+=1
            count2+=(j-i+1)
            
        return count1-count2

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N,L,R = map(int,input().strip().split())
        A = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.countSubarray(N, A, L, R)
        print(ans)

# } Driver Code Ends


