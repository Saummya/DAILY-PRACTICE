#User function Template for python3
class Solution:

	def rowWithMax1s(self,arr, n, m):
		# code here
		count = arr[0].count(1)
		
		for item in arr :
		    count = max(count, item.count(1))
		if count == 0:
            return -1
		i = 0
		for item in arr :
		    if item.count(1) == count :
		        break
		    i += 1
		    
		return i


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = list(map(int, input().strip().split()))
        
        inputLine = list(map(int, input().strip().split()))
        arr = [[0 for j in range(m)] for i in range(n)]
        
        for i in range(n):
            for j in range(m):
                arr[i][j] = inputLine[i * m + j]
        ob = Solution()
        ans = ob.rowWithMax1s(arr, n, m)
        print(ans)
        tc -= 1

# } Driver Code Ends
