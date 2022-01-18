class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        # code here
        
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
        
