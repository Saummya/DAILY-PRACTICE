#User function Template for python3

class Solution:
    def canReach(self, A, N):
        # code here 
        goal=0
        for i in range(N):
            if i>goal:
                return 0
            goal=max(goal,i+A[i])
        return 1

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        A=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.canReach(A,N))
# } Driver Code Ends
