#User function Template for python3

class Solution:

    def findMinDiff(self, A,N,M):

        # code here
        # if there are no chocolates or number
        # of students is 0
        if (M==0 or N==0):
            return 0
    
        # Sort the given packets
        A.sort()
    
        # Number of students cannot be more than
        # number of packets
        if (N < M):
            return -1
            
            # Largest number of chocolates
        min_diff = A[N-1] - A[0]
    
        # Find the subarray of size m such that
        # difference between last (maximum in case
        # of sorted) and first (minimum in case of
        # sorted) elements of subarray is minimum.
        for i in range(len(A) - M + 1):
            min_diff = min(min_diff ,  A[i + M - 1] - A[i])
        
            
        return min_diff
            
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        N = int(input())
        A = [int(x) for x in input().split()]
        M = int(input())


        solObj = Solution()

        print(solObj.findMinDiff(A,N,M))
# } Driver Code Ends