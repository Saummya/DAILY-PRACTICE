'''
You are given N number of books. Every ith book has Ai number of pages and are arranged in sorted order.

You have to allocate contagious books to M number of students. There can be many ways or permutations to do so. In each permutation, one of the M students will be allocated the maximum number of pages. Out of all these permutations, the task is to find that particular permutation in which the maximum number of pages allocated to a student is minimum of those in all the other permutations and print this minimum value.

Each book will be allocated to exactly one student. Each student has to be allocated at least one book.

Note: Return -1 if a valid assignment is not possible, and allotment should be in contiguous order (see the explanation for better understanding).

 

Example 1:

Input:
N = 4
A[] = {12,34,67,90}
M = 2
Output:113
Explanation:Allocation can be done in 
following ways:{12} and {34, 67, 90} 
Maximum Pages = 191{12, 34} and {67, 90} 
Maximum Pages = 157{12, 34, 67} and {90} 
Maximum Pages =113. Therefore, the minimum 
of these cases is 113, which is selected 
as the output.

Example 2:

Input:
N = 3
A[] = {15,17,20}
M = 2
Output:32
Explanation: Allocation is done as
{15,17} and {20}
Your Task:
You don't need to read input or print anything. Your task is to complete the function findPages() which takes 2 Integers N, and m and an array A[] of length N as input and returns the expected answer.


Expected Time Complexity: O(NlogN)
Expected Auxilliary Space: O(1)


Constraints:
1 <= N <= 105
1 <= A [ i ] <= 106
1 <= M <= 105

 '''
class Solution:
    
    #Function to find minimum number of pages.
  
    def findPages(self,A, N, M):
        #code here
        #The task is to assign books
        # in such a way that the maximum number of pages assigned to a student is minimum. 
        ans=-1
        l=min(A)
        h=sum(A)
        while l<=h:
            mid=l+(h-l)//2
            if check(A,M,mid):
                ans=mid
                h=mid-1
            else:
                l=mid+1
        return ans  
        
def check(A,M,mid):
    studentCount=1
    ans=0
    for i in A:
        if i>mid:
            return False
        ans+=i
        if ans>mid:
            ans=i
            studentCount+=1
                
    if studentCount>M:
        return False
    else: 
        return True
    
        
  


#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        n=int(input())
        
        arr=[int(x) for x in input().strip().split()]
        m=int(input())
        
        ob=Solution()
        
        print(ob.findPages(arr,n,m))
# } Driver Code Ends
'''
APPROACH-
Given number of pages in n different books and m students. The books are arranged in ascending order of number of
pages. Every student is assigned to read some consecutive books. The task is to assign books in such a way that 
the maximum number of pages assigned to a student is minimum. 

The idea is to use Binary Search. We fix a value for the number of pages as mid of current minimum and maximum. 
We initialize minimum and maximum as 0 and sum-of-all-pages respectively. If a current mid can be a solution, 
then we search on the lower half, else we search in higher half.
Now the question arises, how to check if a mid value is feasible or not? Basically, we need to check if we can assign
pages to all students in a way that the maximum number doesn't exceed current value. To do this, we sequentially assign pages
to every student while the current number of assigned pages doesn't exceed the value. In this process, if the number of students 
becomes more than m, then the solution is not feasible. Else feasible.
'''



