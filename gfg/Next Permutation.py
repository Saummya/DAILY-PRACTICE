#link-->https://practice.geeksforgeeks.org/problems/next-permutation5226/1/?category[]=Arrays&category[]=Arrays&problemType=functional&page=1&sortBy=submissions&company[]=Infosys&query=category[]ArraysproblemTypefunctionalpage1sortBysubmissionscompany[]Infosyscategory[]Arrays
'''
Implement the next permutation, which rearranges the list of numbers into Lexicographically next greater permutation of list of numbers. If such arrangement is not possible, it must be rearranged to the lowest possible order i.e. sorted in an ascending order. You are given an list of numbers arr[ ] of size N.

Example 1:

Input: N = 6
arr = {1, 2, 3, 6, 5, 4}
Output: {1, 2, 4, 3, 5, 6}
Explaination: The next permutation of the 
given array is {1, 2, 4, 3, 5, 6}.
Example 2:

Input: N = 3
arr = {3, 2, 1}
Output: {1, 2, 3}
Explaination: As arr[] is the last 
permutation. So, the next permutation 
is the lowest one.
Your Task:
You do not need to read input or print anything. Your task is to complete the function nextPermutation() which takes N and arr[ ] as input parameters and returns a list of numbers containing the next permutation.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ N ≤ 10000
'''
#SOLUTION
#User function Template for python3

class Solution:
    def nextPermutation(self, N, arr):
        # code here
        # 4,1,3,2
        # 0,1,2,3
        #Works only for:
        #Input: N = 6
        #arr = {1, 2, 3, 6, 5, 4}
        #Output: {1, 2, 4, 3, 5, 6}
        
        for i in range(N-1,0,-1):
            if arr[i]>arr[i-1]:
                k1=arr[i-1]
                ind1=i-1
                break
            if i==1 and arr[i]>arr[i-1]:
                return sorted(arr)
            
        min1=arr[k1+1]
        for i in range(ind1+2,N):
            if min1>arr[i]:
                min1=arr[i]
                ind2=i
                break
            
        arr[ind1],arr[ind2]=arr[ind2],arr[ind1]
        
        arr1=sorted(arr[ind1+1:])
        arr2=arr[:ind1+1]
        newarr=[]
        for ele in arr2:
            newarr.append(ele)
        for el in arr1:
            newarr.append(el)
        
        return newarr
      
      #------------------------------------------------------------------------
      #APPROACH2
      
class Solution:
    def nextPermutation(self, N, arr):
        # code here
        # 4,1,3,2
        # 0,1,2,3
        for i in range(N-1,0,-1):
            ind1=0
            if arr[i]>arr[i-1]:
                #k1=arr[i-1]
                ind1=i-1 #3
                break
            
            if i==1 and arr[i]>arr[i-1]:
                return sorted(arr)
            
        x=arr[ind1]
        smallest=ind1+1
        for j in range(ind1+2,N):
            if arr[j]>x and arr[j]<arr[smallest]:
                smallest=j
                
        arr[smallest],arr[ind1]=arr[ind1],arr[smallest]
        X=0
        #converting list upto ind1 into a number
        for j in range(ind1+1):
            X=X*10+arr[j]
        
        arr=sorted(arr[ind1+1:])
        for j in range(N-(ind1+1)):
            X=X*10+arr[j]
        
        arr1=list(map(int,X))
        return arr1
      #----------------------------------------------------------------------------------
      #APPROACH3
      #FINAL APPROACH
      #User function Template for python3

class Solution:
    def nextPermutation(self, N, arr):
        # code here
                # code here
        # 4,1,3,2
        # 0,1,2,3
        k=N-2
        while k >= 0:
            if arr[k] < arr[k + 1]:
                break
            k -= 1
            
        # reverse the list if the digit that is smaller than the
        # digit next to it is not found.
        if k < 0:
            arr = arr[::-1]
        else:
            
             # find the first greatest element than arr[k] from the 
                # end of the list
            for l in range(N - 1, k, -1):
                if arr[l] > arr[k]:
                    break
            # swap the elements at arr[k] and arr[l      
            arr[l], arr[k] = arr[k], arr[l]
            
            # reverse the list from k + 1 to the end to find the 
            # most nearest greater number to the given input number
            arr[k + 1:] = reversed(arr[k + 1:])
    
        return arr
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        ans = ob.nextPermutation(N, arr)
        for i in range(N):
            print(ans[i],end=" ")
        print()
# } Driver Code Ends

'''
APPROACH

You can now try developing an algorithm yourself. 
Following is the algorithm for finding the next greater number. 
I) Traverse the given number from rightmost digit, keep traversing till you find a digit which is smaller than the previously traversed digit. For example, if the input number is "534976", we stop at 4 because 4 is smaller than next digit 9. If we do not find such a digit, then output is "Not Possible".




II) Now search the right side of above found digit 'd' for the smallest digit greater than 'd'. For "534976", the right side of 4 contains "976". The smallest digit greater than 4 is 6.




III) Swap the above found two digits, we get 536974 in above example.




IV) Now sort all digits from position next to 'd' to the end of number. The number that we get after sorting is the output. For above example, we sort digits in bold 536974. We get "536479" which is the next greater number for input 534976.
'''
            
            
