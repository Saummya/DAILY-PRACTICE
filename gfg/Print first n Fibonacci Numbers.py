'''
LINK
https://practice.geeksforgeeks.org/problems/print-first-n-fibonacci-numbers1002/1/?company[]=Infosys&company[]=Infosys&problemType=functional&page=1&sortBy=submissions&query=company[]InfosysproblemTypefunctionalpage1sortBysubmissionscompany[]Infosys#
'''

'''
Given a number N, find the first N Fibonacci numbers. The first two number of the series are 1 and 1.

Example 1:

Input:
N = 5
Output: 1 1 2 3 5
Example 2:

Input:
N = 7
Output: 1 1 2 3 5 8 13
Your Task:
Your task is to complete printFibb() which takes single argument N and returns a list of first N Fibonacci numbers.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).
'''
#User function Template for python3

class Solution:
    #Function to return list containing first n fibonacci numbers.
    def printFibb(self,n):
        # your code here
        arr=[]
        #arr[0]=1
        #arr[1]=1
        a1=1
        a2=1
        if n==1:
            arr.append(1)
            return arr
        if n==2:
            arr.append(1)
            arr.append(1)
            return arr
        
        arr.append(a1)
        arr.append(a2)
        for i in range(2,n):
            a3=a1+a2
            a1=a2
            a2=a3
            arr.append(a3)
            
            
        return arr

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    t=int(input())
    for tcs in range(t):
        
        n=int(input())
        res = Solution().printFibb(n)
        for i in range (len (res)):
            print (res[i], end = " ") 
        print()
# } Driver Code Ends
