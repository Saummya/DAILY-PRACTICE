 #User function Template for python3
 
class Solution:
    
    # arr[] : the input array
    # N : size of the array arr[]
    
    #Function to return length of longest subsequence of consecutive integers.
    def findLongestConseqSubseq(self,arr, N):
        #code here
        ans = 0
        count = 0
    
        # Sort the array 
        arr.sort()
    
        v = []
    
        v.append(arr[0])
    
        # Insert repeated elements only 
        # once in the vector 
        for i in range(1, N):
            if (arr[i] != arr[i - 1]):
                v.append(arr[i])
    
        # Find the maximum length 
        # by traversing the array 
        for i in range(len(v)):
    
            # Check if the current element is
            # equal to previous element +1 
            if (i > 0 and v[i] == v[i - 1] + 1):
                count += 1
                
            # Reset the count 
            else:
                count = 1
                
            # Update the maximum 
            ans = max(ans, count)
            
        return ans

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

if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n=int(input())
        a = list(map(int, input().strip().split()))
        print(Solution().findLongestConseqSubseq(a,n))
# } Driver Code Ends