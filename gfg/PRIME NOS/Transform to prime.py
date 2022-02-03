'''
Given an array of n integers. Find the minimum positive number to be inserted in array, so that sum of all elements of array becomes prime. If sum is already prime, then return 0.

 

Example 1:

Input:
N=5
arr[] = { 2, 4, 6, 8, 12 }
Output:  5
Explanation: 
The sum of the array is 32 ,we can add
5 to this to make it 37 which is a
prime number .

Example 2:

Input:
N=3
arr[] = { 1, 5, 7 }
Output:  0 
Explanation: 
The sum of the array is 13 
which is already prime. 

Your Task:
You don't need to read input or print anything. Your task is to complete the function minNumber() that takes array arr and integer N as input parameters and returns the minimum positive number to be inserted in the array so as to make it's sum a prime number.

 

Expected Time Complexity: O(N log(log N))
Expected Auxiliary Space: O(1).

 

Constraints:
1 ≤ N ≤ 105
'''
#User function Template for python3

import math

def minNumber(arr,N):
    # code here
    sum1=sum(arr)
    if isprime(sum1):
        return 0
    c=0
    while not isprime(sum1):
        sum1+=1
        c+=1
    return c
        
        
        
def isprime(n):
    if n==1 or n==0:
        return 0
    if n==2 or n==3:
        return 1
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return 0
    return 1


#{ 
#  Driver Code Starts
#Initial Template for Python 3


t=int(input())
for _ in range(0,t):
    n=int(input())
 #    l=list(map(int,input().split()))
 #    n=l[0]
 #    m=l[1]
    a=list(map(int,input().split()))
   # k = int(input())
  #  b = list(map(int, input().split()))
    ans=minNumber(a,n)
    print(ans)

# } Driver Code Ends
