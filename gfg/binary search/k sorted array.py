'''
Given an array of n distinct elements. Check whether the given array is a k sorted array or not. A k sorted array is an array where each element is at most k distance away from its target position in the sorted array.


Example 1:

Input:
N=6
arr[] = {3, 2, 1, 5, 6, 4} 
K = 2
Output: Yes
Explanation:
Every element is at most 2 distance 
away from its target position in the
sorted array.  
Example 2:

Input:
N=7
arr[] = {13, 8, 10, 7, 15, 14, 12}
K = 1
Output: No

Your Task:
Since, this is a function problem. You don't need to take any input, as it is already accomplished by the driver code. You just need to complete the function isKSortedArray() that takes array arr, integer n and integer k as parameters and return "Yes" if the array is a k sorted array else return "No".


Expected Time Complexity: O(NlogN).
Expected Auxiliary Space: O(N).


Constraints:
1 ≤ N ≤ 105
0 ≤ K ≤ N
'''
#User function Template for python3
from collections import defaultdict
class Solution:
    def isKSortedArray(self, arr, n, k): 
        #code here.
        d=defaultdict(lambda:0)
        ind=0
        for i in arr:
            d[i]=ind
            ind+=1
        arr.sort()
        for i in range(n):
            if abs(d[arr[i]]-i)>k:
                return "No"
        return "Yes"



#{ 
#  Driver Code Starts
#Initial Template for Python 3

t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    k=int(input())
    ob = Solution()
    print(ob.isKSortedArray(a, n, k))

# } Driver Code Ends
