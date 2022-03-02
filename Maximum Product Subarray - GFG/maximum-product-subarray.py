#User function Template for python3
class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr, n):
		# code here
		maxsum=0
        tempsum=1
        if n==1:
            return arr[0]
        for i in range (n):
            tempsum*=arr[i]
            maxsum=max(maxsum,tempsum)
            if tempsum==0:
                tempsum=1
                
        tempsum=1    
        for i in range (n-1,-1,-1):
            tempsum*=arr[i]
            maxsum=max(maxsum,tempsum)
            if tempsum==0:
                tempsum=1
            
               
        return maxsum

#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends