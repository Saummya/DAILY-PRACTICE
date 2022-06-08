#User function Template for python3

class Solution:
	def streamAvg(self, arr, n):
		# code here
		l= []
        sm =0
        for x in range(len(arr)):
            sm+=arr[x]
            a = sm/(x+1)
            l.append(a)
        return l

		

#{ 
#  Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.streamAvg(arr, n)
        for x in ans:
            print('%.2f'%x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends