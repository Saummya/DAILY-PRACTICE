'''
Given an array with N elements, the task is to find the count of factors of a number X which is product of all array elements.
 

Example 1:

Input:
N = 3
Arr[] = {2, 4, 6}
Output:
10
Explanation:
2 * 4 * 6 = 48, the factors of 48 are 
1, 2, 3, 4, 6, 8, 12, 16, 24, 48
whose count is 10.
 

Example 2:

Input:
N = 3
Arr[] = {3, 5, 7}
Output:
8
Explanation:
3 * 5 * 7 = 105, the factors of 105 are 
1, 3, 5, 7, 15, 21, 35, 105 whose count is 8.
 

Your Task:  
You don't need to read input or print anything. Your task is to complete the function countDivisorsMult() which takes the array A[] and its size N as inputs and returns the count of factors of X.

 

Expected Time Complexity: O(N. sqrt(N))
Expected Auxiliary Space: O(N)

 

Constraints:
2<=N<=102
1<=Arr[i]<=102
'''
#User function Template for python3
import math
from collections import defaultdict
class Solution:
    def checkprimebysieve(self,largest, prime):
 
    # Create a boolean array "isPrime[0..n]" and initialize
    # all entries it as true. A value in isPrime[i] will
        # finally be false if i is Not a isPrime, else true.
        isPrime = [True] * (largest + 1)
     
        p = 2
        while p * p <= largest:
     
            # If isPrime[p] is not changed, then it is a isPrime
            if (isPrime[p] == True):
     
                # Update all multiples of p
                for i in range(p * 2, largest + 1, p):
                    isPrime[i] = False
            p += 1
     
        # Print all isPrime numbers
        for p in range(2, largest + 1):
            if (isPrime[p]):
                prime.append(p)
                
 
    
    def countDivisorsMult(self, a, n):
        # Find all prime numbers smaller than
        # the largest element.
        largest = max(a)
        prime = []
        self.checkprimebysieve(largest, prime)
     
        # Find counts of occurrences of each prime
        # factor
        mp = defaultdict(int)
        for i in range(n):
            for j in range(len(prime)):
                while(a[i] > 1 and a[i] % prime[j] == 0):
                    a[i] //= prime[j]
                    mp[prime[j]] += 1
            if (a[i] != 1):
                mp[a[i]] += 1
            
        # Compute count of all divisors using counts
        # prime factors.
        res = 1
        for it in mp.values():
            res *= (it + 1)
        return res

   

#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        
        print(Solution().countDivisorsMult(a, n))
        
        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends
