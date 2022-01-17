#User function Template for python3
class Solution:
    def smallestNumber (self, S, D):
        # code here 
        
        i=0
        d=D
        s=S
        while(True):
            arr=["0"]*d
            x=max(1,s-9*(d-1))
            if x>9:
                return -1
            arr[0]=str(x)
            s=s-x
            for i in range (d-1,0,-1):
                y=min(s,9)
                arr[i]=str(y)
                s=s-y
            return ''.join(arr)
        '''
        arr=["0"]*D
        n=D-1
        s=S
        
        while n>=0:
            for i in range(D):
                if s>9:
                    arr[n]=9
                else:
                    arr[n]=s-1
                    
                n-=1
                s=s-arr[n]
                
        Str1 = ' '.join([str(elem) for elem in arr])
        k= "".join(arr)
        return k
        '''
        
       
        
        # code here 
        '''
        if s/9>d:
            return -1
        num=""
        s-=1
        for i in range(d-1):
            if s>=9:
                num="9"+num
                s-=9
            else:
                num=str(s)+num
                s=0
        return str(s+1)+ num
      
            '''
            
            
            
            


#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S,D=map(int,input().strip().split(" "))

        ob = Solution()
        print(ob.smallestNumber(S,D))
# } Driver Code Ends
