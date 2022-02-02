'''
Given two arrays of A and B respectively of sizes N1 and N2, the task is to calculate the product of the maximum element of the first array and minimum element of the second array.

Example 1:

Input : A[] = {5, 7, 9, 3, 6, 2}, 
        B[] = {1, 2, 6, -1, 0, 9}
Output : -9
Explanation:
The first array is 5 7 9 3 6 2. 
The max element among these elements is 9.
The second array is 1 2 6 -1 0 9.
The min element among these elements is -1.
The product of 9 and -1 is 9*-1=-9.

Example 2:

Input : A[] = {0, 0, 0, 0}, 
           B[] = {1, -1, 2}
Output : 0

Your Task:
This is a function problem. The input is already taken care of by the driver code. You only need to complete the function find_multiplication() that takes an array of integer (A), another array of integer (B), size of array A(n), size of array B(m) and return the product of the max element of the first array and the minimum element of the second array. The driver code takes care of the printing.

Expected Time Complexity: O(N + M).
Expected Auxiliary Space: O(1).
 

Output:
For each test case, output the product of the max element of the first array and the minimum element of the second array.

Constraints:
1 ≤ N, M ≤ 106
-108 ≤ Ai, Bi ≤ 108
'''
#User function Template for python3

class Solution:
    def find_multiplication (self, arr, brr, n, m) : 
        #Complete the function
        k=max(arr)
        l=min(brr)
        res=k*l
        return res


#{ 
#  Driver Code Starts
#Initial Template for Python 3

    
    
for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    m = int(input())
    brr = list(map(int,input().strip().split()))
    ob=Solution()
    res = ob.find_multiplication(arr, brr, n, m)
    print(res)






# } Driver Code Ends
