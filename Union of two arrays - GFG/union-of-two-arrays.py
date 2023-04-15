#User function Template for python3

class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def doUnion(self,a,n,b,m):
        
        #code here
        '''
        s=set()
        
        for i in range(n):
            s.add(a[i])
            
        for i in range(m):
            s.add(b[i])
            
        return len(s)
        '''
        
        a=set(a)
        b=set(b)
        
        return len(a.union(b))
       

#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        n,m=[int(x) for x in input().strip().split()]
        
        a=[int(x) for x in input().strip().split()]
        b=[int(x) for x in input().strip().split()]
        ob=Solution()
        
        print(ob.doUnion(a,n,b,m))
# } Driver Code Ends