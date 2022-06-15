class Solution:
    def smallestSubWithSum(self, a, n, x):
        # Your code goes here 
        c=1000000000
        left=0
        sum1=0
        n=len(a)
        for i in range(n):
            sum1+=a[i]
           
            while sum1>x:
                c=min(c,i-left+1)
                sum1-=a[left]
                left+=1
        return c
        


#{ 
#  Driver Code Starts
def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m = sz[0], sz[1]
        a = [int(x) for x in input().strip().split()]
        print(Solution().smallestSubWithSum(a, n, m))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends