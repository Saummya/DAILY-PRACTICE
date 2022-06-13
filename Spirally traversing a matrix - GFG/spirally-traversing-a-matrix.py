#User function Template for python3

class Solution:
    
    #Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self,matrix, r, c): 
        # code here 
        '''
        make 4 points top = 0 , right = c-1, bottom = r-1, left = 0;
        Run a loop top to right
        then top to bottom,
        bottom row , right to left column
        left column , bottom to top row
        '''
        top=0
        right=c-1
        bottom=r-1
        left=0
        l=[]
        
        while (top<=bottom and right>=left):
            for i in range(left,right+1):
                l.append(matrix[top][i])
            top+=1
            for i in range(top, bottom+1):
                l.append(matrix[i][right])
            right-=1
            if top<=bottom:
                for i in range(right,left-1,-1):
                    l.append(matrix[bottom][i])
                bottom-=1
            if left<=right:
                for i in range(bottom,top-1,-1):
                    l.append(matrix[i][left])
                left+=1
        return l
            
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r,c = map(int, input().strip().split())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix =[]
        for i in range(r):
            row=[]
            for j in range(c):
                row.append(values[k])
                k+=1
            matrix.append(row)
        obj = Solution()
        ans = obj.spirallyTraverse(matrix,r,c)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends