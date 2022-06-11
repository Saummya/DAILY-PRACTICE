#User function Template for python3

class Solution:
	def find_median(self, v):
		# Code here
		n=len(v)
		v.sort()
		if n%2!=0:
		    mid=n//2
		    return v[mid]
		    
		else:
		    m1=n//2
		    m2=(n//2)-1
		    av=(v[m1]+v[m2])//2
		    return av

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		v = list(map(int,input().split())) 
		ob = Solution();
		ans = ob.find_median(v)
		print(ans)
# } Driver Code Ends