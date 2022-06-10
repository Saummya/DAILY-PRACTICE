#User function Template for python3
class Solution: 
    def firstAndLast(self, arr, n, x): 
        # Code here
        
        
        list1 = []
        a=arr[::-1]
        if x not in arr:
            list1.append(-1)
            return list1
        return arr.index(x), len(a)-a.index(x)-1
        
        '''
        
        def first(arr,n,x):
            st=0
            en=n-1
            a1=0
            while st<=en:
                mid=st+(en-st)//2
                if( ( mid == 0 or x > arr[mid - 1]) and arr[mid] == x) :
                    return mid
                elif (x > arr[mid]) :
                    st=mid+1
                    return first(arr, x, n)
                else :
                    en=mid-1
                    return first(arr, x, n)
                return -1
                
        def last(arr,n,x):
            st=0
            en=n-1
            a2=0
            while st<=en:
                mid=st+(en-st)//2
                if( ( mid == n-1 or x<arr[mid+1]) and arr[mid] == x) :
                    return mid
                elif (x > arr[mid]) :
                    st=mid+1
                    return last(arr, x, n)
                else :
                    en=mid-1
                    return last(arr, x, n)
                return -1'''
                
        
     
                    
                    
                    
                   
                    
                

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input()) 
    for _ in range(t):
        n,x = [int(i) for i in input().split()] 
        arr = [int(i) for i in input().split()] 
        ob=Solution() 
        ans=ob.firstAndLast(arr,n,x) 
        s=(" ").join(map(str,ans))
        print(s)

# } Driver Code Ends