#User function Template for python3
class Solution:

	def fascinating(self,n):
	    # code here
	    
	        
	        a=n*2
	        b=n*3
	        n2=str(a)+str(b)+str(n)
	        l=list(n2)
	        l.sort()
	        sum=""
	        for i in l:
	            sum=sum+i
	        if(sum=="123456789"):
	            return True
	        else:
	            return False
	   
        
	

#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input().strip())
        ob = Solution()
        ans = ob.fascinating(n)
        if ans:
            print("Fascinating")
        else:
            print("Not Fascinating")
        tc -= 1

# } Driver Code Ends