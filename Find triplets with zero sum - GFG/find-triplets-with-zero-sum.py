#User function Template for python3

class Solution:
    #Function to find triplets with zero sum.    
    def findTriplets(self, arr, n):
        #code here
        '''
        for i in range(len(arr)):
           for j in range(i+1,len(arr)):
               for k in range(j+1, len(arr)):
                   if (arr[i] + arr[j] + arr[k]) == 0:
                       return 1
        return 0'''
        
        arr.sort()
        for i in range(n):
            low=i+1
            high=n-1
            while low<high:
                if arr[low]+arr[high]<-arr[i]:
                    low+=1
                elif arr[low]+arr[high]>-arr[i]:
                    high-=1
                else:
                    return True
        return False
                

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n=int(input())
        a=list(map(int,input().strip().split()))
        if(Solution().findTriplets(a,n)):
            print(1)
        else:
            print(0)
# } Driver Code Ends