#User function template for Python

class Solution:
    #Function to find the days of buying and selling stock for max profit.
	def stockBuySell(self, A, n):
		#code here
		v=[]
        for i in range(len(A)-1):
            if A[i]<A[i+1]:
                v.append([i,i+1])
        return v
		
		'''
		#APPROACH2
		flag=0
		a1=A
		a1.sort()
		k,l=0,0
		
		for i in range(n):
		    a=0
        	b=n-1
		    while a<b:
    		    
        		min=a1[a]
        		max=a1[b]
    		
    		    if A[i]==min:
    		        k=i
    		    elif A[i]==max:
    		        l=i
    		    else:
    		        continue
    		    
    		    if k<l:
    		        flag==1
    		    else:
    		        a+=1
    		        b-=1
    	if flag==1:
    	    return 1
    	else:
    	    return 0
    	'''
		        

#{ 
#  Driver Code Starts
#Initial template for Python

def check(ans,A,p):
    c = 0
    for i in range(len(ans)):
        c += A[ans[i][1]]-A[ans[i][0]]
    if(c==p):
        return 1 
    else:
        return 0

if __name__=='__main__':
	t = int(input())
	while(t>0):
		n = int(input())
		A = [int(x) for x in input().strip().split()]
		ob = Solution()
		ans = ob.stockBuySell(A,n)
		p=0
		for i in range(n-1):
		    p += max(0,A[i+1]-A[i])
		if(len(ans) == 0):
			print("No Profit",end="")
		else:
			print(check(ans,A,p),end="")
		print()
		t-=1
# } Driver Code Ends
