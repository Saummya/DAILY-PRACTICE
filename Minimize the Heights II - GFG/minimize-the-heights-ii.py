#User function Template for python3

class Solution:
    def getMinDiff(self, arr, n, k):
        # code 
    
        arr=sorted(arr)
        max_ele=max(arr)
        min_ele=min(arr)
        result=arr[n-1]-arr[0]
        
        for i in range(n):
            max_ele=max(arr[i-1]+k,arr[n-1]-k)
            min_ele=min(arr[i]-k,arr[0]+k)
            
            if min_ele<0:
                continue
            result=min(result,max_ele-min_ele)
        return result
            
            
        '''
            if arr[i]<k+1:
                arr[i]=arr[i]+k
            else:
                arr[i]-=k
            
        k1=arr[n-1]
        k2=arr[0]
        return k1-k2'''

#{ 
#  Driver Code Starts
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