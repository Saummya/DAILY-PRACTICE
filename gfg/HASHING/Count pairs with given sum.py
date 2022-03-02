#User function Template for python3

class Solution:
    def getPairsCount(self, arr, n, k):
        # code here
        m = [0] * 2000000
  
        for i in range(0, n):
            m[arr[i]] += 1
            
        twice_count = 0
    
        for i in range(0, n):
            twice_count += m[k - arr[i]]
            if (k - arr[i] == arr[i]):
                twice_count -= 1
     

        return int(twice_count / 2)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getPairsCount(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends
