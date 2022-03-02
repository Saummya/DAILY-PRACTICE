'''
Given an array A of positive integers. Your task is to find the leaders in the array. An element of array is leader if it is greater than or equal to all the elements to its right side. The rightmost element is always a leader. 

 

Example 1:

Input:
n = 6
A[] = {16,17,4,3,5,2}
Output: 17 5 2
Explanation: The first leader is 17 
as it is greater than all the elements
to its right.  Similarly, the next 
leader is 5. The right most element 
is always a leader so it is also 
included.
 

Example 2:

Input:
n = 5
A[] = {1,2,3,4,0}
Output: 4 0
 

Your Task:
You don't need to read input or print anything. The task is to complete the function leader() which takes array A and n as input parameters and returns an array of leaders in order of their appearance.

 

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)

 

Constraints:
1 <= n <= 107
0 <= Ai <= 107
'''


class Solution:
    #Back-end complete function Template for Python 3
    
    #Function to find the leaders in the array.
    def leaders(self, A, N):
        #Code here
        ans=[]
        final_ans=[]
        maxi=-1   #taking the last element
        for val in reversed(A):
            maxi=max(maxi,val)
            if(maxi==val):
                ans.append(val)
                
        # for i in range(len(ans),-1,-1):
        #     final_ans.append(ans[i])
            
        return reversed(ans)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math


    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        N=int(input())
        
        A=[int(x) for x in input().strip().split()]
        obj = Solution()
        
        A=obj.leaders(A,N)
        
        for i in A:
            print(i,end=" ")
        print()
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends
