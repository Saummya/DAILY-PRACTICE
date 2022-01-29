'''
Given is a range of integers [a , b]  . You have to find the sum of all the numbers in the range  [a , b] that are prime as well as palindrome.

 

Example 1:

Input:
a = 1, b = 10
Output:
17
Explanation:
prime numbers between 1 and 10 are 2, 3,
5, and 7. All of these are Palindromes.
So, sum = 17.
Example 2:

Input:
a = 11, b = 13
Output:
11
Explanation:
prime numbers between 11 and 13 are 11
and 13. Omly 11 is Palindrome among these.
So, sum = 11. 
 

Your Task:
You don't need to read input or print anything. Your task is to complete the function getPPS() which takes 2 Integers a and b as input and returns an integer as the answer.

 

Expected Time Complexity: O(loglog(B))
Expected Auxiliary Space: O(B)

 

Constraints:
1 <= A <= B <= 105
'''
#User function Template for python3
import math
class Solution:
    def getPPS(self, a, b):
        # code here 
        sum1=0
        for i in range(a,b+1):
            if isprime(i)==1:
                if ispalindrome(i)==True:
                    sum1+=i
        return sum1
   
   
        
def isprime(n):
    if n==1 or n==0:
        return 0
    if n==2 or n==3:
        return 1
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return 0
    return 1

def ispalindrome(n):
    n1=str(n)
    if (n1==n1[::-1]):
        return True
    else:
        return False
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        a,b=map(int,input().split()) 
        
        ob = Solution()
        print(ob.getPPS(a,b))
# } Driver Code Ends
