#User function Template for python3

class Solution:
    #Function to return the largest possible number of n digits
    #with sum equal to given sum.
    def largestNum(self,n,s):
        
        # code here
        if s>n*9:
            return -1
        else:
            j=0
            k=0
            while(s>9):
                j=10*j+9
                s=s-9
                k+=1
            s=10*j+s
            for i in range(n-k-1):
                s=s*10
        return s
                
    
