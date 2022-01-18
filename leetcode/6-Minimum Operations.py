#User function Template for python3

class Solution:
    def minOperation(self, n):
        # code here 
        count=0
        while n>0:
            if n%2==0:
                n=n/2
                count+=1
            else:
                n-=1
                count+=1
                
        return count
