'''
You are given an array A, of N elements. Find minimum index based distance between two elements of the array, x and y.

Example 1:

Input:
N = 4
A[] = {1,2,3,2}
x = 1, y = 2
Output: 1
Explanation: x = 1 and y = 2. There are
two distances between x and y, which are
1 and 3 out of which the least is 1.
Example 2:

Input:
N = 7
A[] = {86,39,90,67,84,66,62}
x = 42, y = 12
Output: -1
Explanation: x = 42 and y = 12. We return
-1 as x and y don't exist in the array.
Your Task:
Complete the function minDist() which takes the array, n, x and y as input parameters and returns the minimum distance between x and y in the array. If no such distance is possible then return -1.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
1 <= N <= 105
0 <= A[i], x, y <= 105'''

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
