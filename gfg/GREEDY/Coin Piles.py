'''
There are N piles of coins each containing  Ai (1<=i<=N) coins. Find the minimum number of coins to be removed such that the absolute difference of coins in any two piles is at most K.
Note: You can also remove a pile by removing all the coins of that pile.


Example 1:

Input:
N = 4, K = 0
arr[] = {2, 2, 2, 2}
Output:
0
Explanation:
For any two piles the difference in the
number of coins is <=0. So no need to
remove any coins. 
Example 2:
Input:
N = 6, K = 3
arr[] = {1, 5, 1, 2, 5, 1} 
Output :
2
Explanation:
If we remove one coin each from both
the piles containing 5 coins , then
for any two piles the absolute difference
in the number of coins is <=3. 


Your Task:  
You don't need to read input or print anything. Your task is to complete the function minSteps() which takes 2 integers N, and K and an array A of size N as input and returns the minimum number of coins that need to be removed.


Expected Time Complexity: O(N*logN)
Expected Auxiliary Space: O(N)


Constraints:
1 ≤ N ≤ 105
0 ≤ K ≤ 103
1 ≤ A[i] ≤ 103
'''

#Solution:
'''
In order to find the minimum number of coins to be added, we iterate over all the coin pile sizes,
and for the rest of the piles if the pile size is less than the current size then remove that pile entirely
otherwise if the pile size is greater than current pile size plus K then remove the excess coins. The minimum
number of coins removed in any of the turns is the answer.
'''
#User function Template for python3

class Solution:
    def minSteps(self, A, N, K):
        # code here 
        def upper_bound(l, r, val):
            pos = r+1
            while l <= r:
                mid = (l+r)//2
                if A[mid] > val:
                    pos = mid
                    r = mid-1
                else:
                    l = mid+1
            return pos
        
        arr = [0]*N
        A.sort()
        arr[0] = A[0]
        for i in range(1, N):
            arr[i] = arr[i-1]+A[i]
            
        ans = 1000000000
        prev = 0
        for i in range(N):
            pos = upper_bound(i, N-1, A[i]+K)
            if i > 0 and A[i] != A[i-1]:
                prev = arr[i-1]
            
            temp = prev + arr[N-1]-arr[pos-1]-(N-pos)*(A[i]+K)
            if temp < ans:
                ans = temp
        return ans
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,K=map(int,input().split())
        A=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.minSteps(A,N,K))
# } Driver Code Ends

