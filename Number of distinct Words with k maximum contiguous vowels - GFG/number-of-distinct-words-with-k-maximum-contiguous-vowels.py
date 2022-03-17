#User function Template for python3

class Solution:
    def kvowelwords(self, N,K):
		# code here
		large = 1000000007
        dp = [1]
        power5 = [1]
        for _ in range(K):
            power5.append((power5[-1]*5)%large)
        for i in range(1,N+1):
            total = 0
            for j in range(min(i+1,K+1)):
                count = power5[j]
                if i>j:
                    count = (count*21*dp[i-j-1])%large
                total = (total + count)%large
            dp.append(total)
        return dp[-1]




#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N,K = map(int,input().split())
		ob = Solution()
		ans = ob.kvowelwords(N,K)
		print(ans)
# } Driver Code Ends