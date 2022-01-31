'''
Ugly numbers are numbers whose only prime factors are 2, 3 or 5. The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, … shows the first 11 ugly numbers. By convention, 1 is included. Write a program to find Nth Ugly Number.

Example 1:

Input:
N = 10
Output: 12
Explanation: 10th ugly number is 12.
Example 2:

Input:
N = 4
Output: 4
Explanation: 4th ugly number is 4.
Your Task:
You don't need to read input or print anything. Your task is to complete the function getNthUglyNo() which takes an integer n as parameters and returns an integer denoting the answer.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)

Constraints:
1 ≤ N ≤ 104
'''
#User function Template for python3
class Solution:
	def getNthUglyNo(self,n):
		# code here
		arr=[1]
		p2=0
		p3=0
		p5=0
		for i in range(2,n+1):
		    num2=arr[p2]*2
            num3=arr[p3]*3
            num5=arr[p5]*5
            res=min(num2,num3,num5)
            arr.append(res)
            if(res==num2):
                p2+=1
            if(res==num3):
                p3+=1
            if(res==num5):
                p5+=1
        return arr[n-1]

#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        ob = Solution()
        ans = ob.getNthUglyNo(n);
        print(ans)
        tc -= 1

# } Driver Code Ends
