'''
LINK
https://practice.geeksforgeeks.org/problems/smallest-positive-missing-number-1587115621/1/?category[]=Arrays&category[]=Arrays&company[]=Amazon&company[]=Amazon&problemType=functional&difficulty[]=1&page=1&sortBy=submissions&query=category[]Arrayscompany[]AmazonproblemTypefunctionaldifficulty[]1page1sortBysubmissionscompany[]Amazoncategory[]Arrays#
'''

'''
You are given an array arr[] of N integers including 0. The task is to find the smallest positive number missing from the array.

Example 1:

Input:
N = 5
arr[] = {1,2,3,4,5}
Output: 6
Explanation: Smallest positive missing 
number is 6.
Example 2:

Input:
N = 5
arr[] = {0,-10,1,3,-20}
Output: 2
Explanation: Smallest positive missing 
number is 2.
Your Task:
The task is to complete the function missingNumber() which returns the smallest positive missing number in the array.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).

Constraints:
1 <= N <= 106
-106 <= arr[i] <= 106
'''
#SOLUTION:
#User function Template for python3

class Solution:
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr,n):
        #Your code here
        x = 1
        s = set(arr)
        while True:
            if x not in s:
                return x
            x = x+1

#{ 
#  Driver Code Starts
#Initial Template for Python 3


import math


def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            print(ob.missingNumber(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends
