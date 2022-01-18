#User function Template for python3

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        # code here
        #compare end[i] with start[i+1] if start[i+1] is greater than end[i] then only meeting will happen.
        a=[]
        for i in range(len(start)):
            a.append([start[i],end[i]])
        a.sort(key=lambda x:x[1])
        j=1
        i=0
        count=1
        while j<n:
            if a[i][1]<a[j][0]:
                count+=1
                i=j
                j+=1
                
            else:
                j+=1
        return count
        

                
                

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.maximumMeetings(n,start,end))
# } Driver Code Ends
