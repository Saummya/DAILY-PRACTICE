'''
Equilibrium index of an array is an index such that the sum of elements at lower indexes is equal to the sum of elements at higher indexes.
Given an array, your task is to find the index of first Equilibrium point in the array.

Input Format:
The first line of input takes an integer T denoting the no of test cases, then T test cases follow. The first line of each test case is an integer N denoting The size of the array. Then in the next line are N space-separated values of the array. 

Output Format:
For each test case, the output will be the equilibrium index of the array. If no such index exists output will be -1.

User Task :
Your task is to complete the function (findEquilibrium) below which returns the index of the first Equilibrium point in the array. The function takes two arguments. The first argument is the array A[ ] and the second argument is the size of the array A.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
1<=T<=100
1<=N<=105
-1000<=A[]<=1000
'''
def findEquilibrium(a,n):
    # Code here
    '''
    for i in range(n):
        if sum(a[:i+1])==sum(a[i+1:]):
            return a[i]
        else:
            return -1'''
    
    s1=0
    s2=0
    for i in range(n):
        s1+=a[i]
    for i in range(n):
        if s1-a[i]==2*s2:
            return i
        s2+=a[i]
    return -1
            
