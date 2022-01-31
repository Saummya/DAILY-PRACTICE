'''
Find the count of numbers less than equal to N having exactly 9 divisors.
 

Example 1:

Input:
N = 100
Output:
2
Explanation:
The two numbers which have 
exactly 9 divisors are 36 and 100.
Example 2:

Input:
N = 1000
Output:
8 
Explanation:
The numbers are:
36 100 196 225 256 441 484 676

Your Task:  
You don't need to read input or print anything. Your task is to complete the function nineDivisors() which takes an integer N as an input parameter and returns the total number of elements from 1 to N inclusive, that have exactly 9 divisors.

Expected Time Complexity: O(sqrt(N))
Expected Auxiliary Space:  O(sqrt(N))
 

Constraints:
1<=N<=1010
'''
#BRUTE FORCE:
class Solution:
    def nineDivisors(self, N):
        # code here 
        c1=0
        for i in range(1,N+1):
            if divisors(i)==9:
                c1+=1
        return c1
        
        
        
def divisors(N):
    count=0
    for i in range(1,N+1):
        if N%i==0:
            count+=1
    return count



#APPROACH USING SIEVE THEOREM:
''' An efficient approach is to use the property of the prime factor to count the number of divisors of a
number. The method can be found here. If any number(let x) can be expressed in terms of (p^2 * q^2) or (p^8), 
where p and q are prime factors of X, then X has a total of 9 divisors. The below steps can be followed to solve the above problem. 

HOW TO?

1. Use Sieve technique to mark the smallest prime factor of a number.
2. We just need to check for all the numbers in the range[1-sqrt(n)] that can be expressed in terms of p*q since (p^2*q^2) has 9 factors, hence (p*q)^2 will also have exactly 9 factors.
3. Iterate from 1 to sqrt(n) and check if i can be expressed as p*q, where p and q are prime numbers.
4. Also, check if i is prime then pow(i, 8)<=n or not, in that case, count that number also.
5. The summation of the count of numbers that can be expressed in the form p*q and p^8 is our answer.
'''
#User function Template for python3
import math 
class Solution:
    def nineDivisors(self, N):
        # code here 
        c=0
        #limit = int(n ** (0.5))
          
         # Sieve array, initially prime[i] = i 
        prime = [i for i in range(int(math.sqrt(N))+1)] 
        
        # use sieve concept to store the 
        # first prime factor of every number 
        i = 2
        while i * i <= int(math.sqrt(N)): 
            if prime[i] == i:
                # mark all factors of i 
                for j in range(i * i, int(math.sqrt(N)) + 1, i): 
                    if prime[j] == j: 
                        prime[j] = i 
          
            i+=1
            
        # check for all numbers if they 
        # can be expressed in form p*q 
        for i in range(2, int(math.sqrt(N)) + 1): 
            
            # p prime factor 
            p = prime[i] 
    
            # q prime factor 
            q = prime[i // prime[i]] 
    
            # if both prime factors are different 
            # if p*q<=n and q!= 
            if p * q == i and q != 1 and p != q: 
                c += 1
                
            elif prime[i] == i: 
    
                # Check if it can be 
                # expressed as p^8 
                if i ** 8 <= N: 
                    c += 1
        
        return c
        

            

#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        ob = Solution()
        print(ob.nineDivisors(N))

# } Driver Code Ends
