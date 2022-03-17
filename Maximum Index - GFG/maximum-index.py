#User function Template for python3

class Solution:
    #Complete this function
    # Function to find the maximum index difference.
    def maxIndexDiff(self,A, N): 
        ##Your code here
        i = 0
        j = N-1
        max1 = 0
        
        while i<N and j>i:
            if A[i]<=A[j] and j>i:
                max1 = max(max1,j-i)
                i+=1
                j=N-1
            else:
                j-=1
            
            if i>=j:
                i+=1
                j=N-1
        
        return max1
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            ob=Solution()
            print(ob.maxIndexDiff(arr,n))
            
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends