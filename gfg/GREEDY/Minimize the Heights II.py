'''
Given an array arr[] denoting heights of N towers and a positive integer K, you have to modify the height of each tower either by increasing or decreasing them by K only once. After modifying, height should be a non-negative integer. 
Find out the minimum possible difference of the height of shortest and longest towers after you have modified each tower.

You can find a slight modification of the problem here.
Note: It is compulsory to increase or decrease (if possible) by K to each tower.


Example 1:

Input:
K = 2, N = 4
Arr[] = {1, 5, 8, 10}
Output:
5
Explanation:
The array can be modified as 
{3, 3, 6, 8}. The difference between 
the largest and the smallest is 8-3 = 5.
Example 2:

Input:
K = 3, N = 5
Arr[] = {3, 9, 12, 16, 20}
Output:
11
Explanation:
The array can be modified as
{6, 12, 9, 13, 17}. The difference between 
the largest and the smallest is 17-6 = 11. 

Your Task:
You don't need to read input or print anything. Your task is to complete the function getMinDiff() which takes the arr[], n and k as input parameters and returns an integer denoting the minimum difference.


Expected Time Complexity: O(N*logN)
Expected Auxiliary Space: O(N)

Constraints
1 ≤ K ≤ 104
1 ≤ N ≤ 105
1 ≤ Arr[i] ≤ 105
'''

#User function Template for python3

class Solution:
    def getMinDiff(self, arr, n, k):
        # code here
        arr=sorted(arr)
        max_ele=max(arr)
        min_ele=min(arr)
        result=arr[n-1]-arr[0]
        
        for i in range(n):
            max_ele=max(arr[i-1]+k,arr[n-1]-k)
            min_ele=min(arr[i]-k,arr[0]+k)
            
            if min_ele<0:
                continue
            result=min(result,max_ele-min_ele)
        return result
            
            
        '''
            if arr[i]<k+1:
                arr[i]=arr[i]+k
            else:
                arr[i]-=k
            
        k1=arr[n-1]
        k2=arr[0]
        return k1-k2'''

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getMinDiff(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends
