
#User function Template for python3

class Solution:
    
    #Function to return list of integers visited in snake pattern in matrix.
    def snakePattern(self, matrix): 
       # code here 
       rows = len(matrix)
       cols = len(matrix[0])
       ans=[]
       for i in range(rows):
           if(i%2==0):
               for j in range(cols):
                #   print(j)
                   ans.append(matrix[i][j])
           else:
               for j in reversed(range(cols)):
                   ans.append(matrix[i][j])
                
                   
       return ans
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix =[]
        for i in range(n):
            row=[]
            for j in range(n):
                row.append(values[k])
                k+=1
            matrix.append(row)
        obj = Solution()
        ans = obj.snakePattern(matrix)
        for i in ans:
            print(i,end=" ")
        print()


# } Driver Code Ends