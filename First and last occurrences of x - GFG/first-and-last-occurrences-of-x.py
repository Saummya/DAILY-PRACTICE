#User function Template for python3


def find(arr,n,x):
    # code here
    #approach1
    '''
    l=[]
    for i in range(n):
        if arr[i]==x:
            l.append(i)
            break
    for i in range(n-1,-1,-1):
        if arr[i]==x:
            l.append(i)
            break
    return l'''
    
    #approach2
    a=-1
    b=-1
    for i in range(n):
        if arr[i]==x:
            if a==-1:
                a=i
            b=i
    return a,b
                


#{ 
#  Driver Code Starts
t=int(input())
for _ in range(0,t):
    l=list(map(int,input().split()))
    n=l[0]
    x=l[1]
    arr=list(map(int,input().split()))
    ans=find(arr,n,x)
    print(*ans)
# } Driver Code Ends