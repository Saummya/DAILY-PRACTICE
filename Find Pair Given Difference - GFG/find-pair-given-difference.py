#User function Template for python3

class Solution:

    def findPair(self, arr, L,N):
        #code here
        arr.sort()
        lo=0
        hi=1
        while lo<L and hi<L:
            if (lo<hi):
                if arr[hi]-arr[lo]==N:
                    return True
                elif arr[hi]-arr[lo]<N:
                    hi+=1
                else:
                    lo+=1
            else:
                hi+=1
                
        
        return False
            
                

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        L,N = [int(x) for x in input().split()]
        arr = [int(x) for x in input().split()]

        solObj = Solution()

        if(solObj.findPair(arr,L, N)):
            print(1)
        else:
            print(-1)
# } Driver Code Ends