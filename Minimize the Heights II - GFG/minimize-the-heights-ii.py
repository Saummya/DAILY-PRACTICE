#User function Template for python3

class Solution:
    def getMinDiff(self, arr, n, k):
        # code here
        arr.sort()
        
        ans = arr[n-1]-arr[0]
        
        curr_min=arr[0]
        curr_max=arr[n-1]
        
        for i in range(1,n):
            if arr[i]<k:
                continue
            
            curr_min=min(arr[0]+k,arr[i]-k)
            
            curr_max=max(arr[n-1]-k,arr[i-1]+k)
            
            ans= min(ans, curr_max-curr_min)
            
        return ans
        
        
       
            



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getMinDiff(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends