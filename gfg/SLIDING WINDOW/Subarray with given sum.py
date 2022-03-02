#User function Template for python3

#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self,arr, n, s): 
       #Write your code here
        f=0
        su_m=0
        for i in range(n):
            su_m+=arr[i]
            if su_m==s:
                l1=[f+1,i+1]
                return l1
            while su_m>s:
                su_m-=arr[f]
                f+=1
                if su_m==s:
                    l1=[f+1,i+1]
                    return l1
            
        l2=[-1]
        return l2
       
       
  
               
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            NS=input().strip().split()
            N=int(NS[0])
            S=int(NS[1])
            
            A=list(map(int,input().split()))
            ob=Solution()
            ans=ob.subArraySum(A, N, S)
            
            for i in ans:
                print(i, end=" ")
                
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends
