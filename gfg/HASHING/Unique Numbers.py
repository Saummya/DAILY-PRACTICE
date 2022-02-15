'''
In the given range [L, R], print all numbers having unique digits. e.g. In range 10 to 20 should print all numbers except 11.

Example 1:

Input:
L = 10
R = 20

Output:
10 12 13 14 15 16 17 18 19 20

Explanation:
The number 11 has two 1 therefore
11 is not a unique number.
Example 2:

Input:
L = 1
R = 9

Output:
1 2 3 4 5 6 7 8 9

Explanation:
All the Numbers are unique.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function uniqueNumbers() which takes two integers L and R as an input parameter and returns the list/vector of all the unique numbers present between L to R.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
1 <= L <= R <= 104
'''
#User function Template for python3
class Solution:
	def uniqueNumbers(self, L, R):
		# code here
		arr=[]
		for i in range(L,R+1):
		    b=str(i)
		    flag=0
		    for z in b:
		        if b.count(z)>1:
		            flag=1
		    if flag==0:
		        arr.append(b)
		return arr

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		l,r = input().split()
		l,r = int(l),int(r)
		
		ob = Solution()
		ans = ob.uniqueNumbers(l,r)
		for a in ans:
			print(a,end = ' ')
		print()

# } Driver Code Ends
