#User function Template for python3

class Solution:
    def longest(self, names, n):
    	# code here
    	max1=0
    	for ele in names:
    	    k=len(ele)
    	    if max1<k:
    	        maxStr= str(ele)
    	        max1=k
    	return maxStr
    	
    	

#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
    	n=int(input())
    	names = []
    	for i in range(n):
    		names.append(input())
    	ob = Solution()
    	print(ob.longest(names, n))
    	
    	T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends