

class Solution:
    def minDist(self, arr, n, x, y):
        diff=1000000
        if x in arr and y in arr:
            z={x:arr.index(x),y:arr.index(y)}
            for i in range(n):
                if arr[i]==x or arr[i]==y:
                    z[arr[i]]=i
                    if diff>abs(z[x]-z[y]):
                        diff=abs(z[x]-z[y])
            return diff
        else:
            return -1
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3


if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        x,y = list(map(int, input().strip().split()))
        print(Solution().minDist(arr, n, x, y))



# } Driver Code Ends