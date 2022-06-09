#User function Template for python3

def getMinMax( a, n):
    max1=a[0]
    min1=a[0]
    
    for i in range(n):
        if max1<a[i]:
            max1=a[i]
    
    for i in range(n):
        if min1>a[i]:
            min1=a[i]
    
    return min1, max1
    
    
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        
        product = getMinMax(a, n)
        print(product[0], end=" ")
        print(product[1])

        T -= 1


if __name__ == "__main__":
    main()



# } Driver Code Ends