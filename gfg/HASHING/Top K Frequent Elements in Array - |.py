'''
Given a non-empty array of integers, find the top k elements which have the highest frequency in the array. If two numbers have the same frequency then the larger number should be given preference. 

Note: Print the elements according to the frequency count (from highest to lowest) 

Example 1:

Input:
N = 6
nums = {1,1,1,2,2,3}
k = 2
Output: {1, 2}
Example 2:

Input:
N = 8
nums = {1,1,2,2,3,3,3,4}
k = 2
Output: {3, 2}
Explanation: Elements 1 and 2 have the
same frequency ie. 2. Therefore, in this
case, the answer includes the element 2
as 2 > 1.
User Task:
The task is to complete the function topK() that takes the array and integer k as input and returns a list of top k frequent elements.

Expected Time Complexity : O(NlogN)
Expected Auxilliary Space : O(N)

Constraints:
1 <= N <= 105
1<=A[i]<=105
'''
class Solution:
	def topK(self, nums, k):
		#Code here
		m = {}
        maxx = max(nums)
        for i in range(1,maxx+1):
            m[i]=0
        for i in range(len(nums)):
            m[nums[i]]+=1
        l = []
        for i in range(1,maxx+1):
            if m[i]!=0:
                l.append([i,m[i]])
        l = sorted(l, key=lambda x:(x[1],x[0]), reverse=True)
        #print(l)
        r = []
        for v in l:
            r.append(v[0])
        return r[:k]
		        

#{ 
#  Driver Code Starts
		
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
    	a = list(map(int, input().strip().split()))
    	n = a[0]
    	nums = a[1:]
    	k = int(input().strip())
    	obj = Solution()
    	ans = obj.topK(nums, k)
    	for i in ans:
    		print(i, end = " ")
    	print()
# } Driver Code Ends
