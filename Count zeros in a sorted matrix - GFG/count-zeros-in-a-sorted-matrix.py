#User function Template for python3
class Solution:
    def countZeroes(self, A, N):
        count=0
        for i in range(N-1,-1,-1):
            for j in range(N):
                if A[i][j]==0:
                    count+=1
                else:
                    break
        return count
                
    
    


#{ 
#  Driver Code Starts
# Your code goes here
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input().strip())
        arr = list(map(int, input().strip().split()))
        matrix = [[0 for i in range(n)]for j in range(n)]
        k=0
        for i in range(n):
            for j in range(n):
                matrix[i][j] = arr[k]
                k+=1
        
        ob = Solution()
        print (ob.countZeroes(matrix, n))
        
# } Driver Code Ends