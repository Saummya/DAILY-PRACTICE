#User function Template for python3

class Solution:
    def minValue(self, a, b, n):
        # Your code goes here
        a.sort()
        b.sort()
        b=b[::-1]
        sum1=0
        for i in range(n):
            p1=a[i]*b[i]
            sum1+=p1
            
        return sum1
        
        #Sort both arrays and reverse on of them them take product of the corresponding elements and add them further.
        
