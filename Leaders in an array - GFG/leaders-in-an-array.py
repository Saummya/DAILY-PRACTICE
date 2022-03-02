

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