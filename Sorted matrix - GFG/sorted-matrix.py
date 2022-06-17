#User function Template for python3

class Solution:
    def sortedMatrix(self,N,Mat):
        #code here
        k=0
        temp = [0]*N*N
        for i in range(N):
            for j in range(N):
                temp[k] = Mat[i][j]
                k +=1
        k=0
        temp.sort()
        for i in range(N):
            for j in range(N):
                Mat[i][j] = temp[k]
                k +=1
        return Mat

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math
        
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        v=[]
        for i in range(N):
            a=list(map(int,input().strip().split()))
            v.append(a)
        ob=Solution()
        ans=ob.sortedMatrix(N,v)
        for i in range(N):
            for j in range(N):
                print(ans[i][j],end=" ")
            print()
# } Driver Code Ends