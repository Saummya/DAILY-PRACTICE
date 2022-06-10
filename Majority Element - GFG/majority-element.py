#User function template for Python 3

class Solution:
    def majorityElement(self, A, N):
        #Your code here
        max1=A[0]
        for i in range(1,N):
            if A[i]>max1:
                max1=A[i]
                
        a=[0]*(max1+1)
        for i in range(N):
            a[A[i]]+=1
            
        for i in range(max1+1):
            if a[i]>N//2:
                return i
        return -1   
            
            
        
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

from sys import stdin


def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            
            obj = Solution()
            print(obj.majorityElement(A,N))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends