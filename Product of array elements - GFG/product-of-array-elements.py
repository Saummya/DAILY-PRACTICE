#User function Template for python3

# arr is the array
# n is the number of element in array
# mod= modulo value
def product(arr,n,mod):
    # your code here
    m=1
    for i in range(n):
        m=(m*arr[i])%mod
    return m

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    t=int(input())
    mod=1000000007
    for j in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        print(product(arr,n,mod))
# } Driver Code Ends