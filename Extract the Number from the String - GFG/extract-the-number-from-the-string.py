class Solution:
    def ExtractNumber(self,S):
        #code here
        l=[]
        a=[]
        for i in S.split():
            if i.isdigit():
               l.append(i)
        for i in l:
            if '9' not in i:
                a.append(int(i))
        if len(a)!=0:
            return max(a)
        else:
            return -1
           

#{ 
#  Driver Code Starts
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        S=input()
        ob=Solution()
        ans=ob.ExtractNumber(S)
        print(ans)   
# } Driver Code Ends