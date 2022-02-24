#User function Template for python3


class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def isAnagram(self,a,b):
        #code here
        if len(a)!=len(b):
            return False
        da={}
        db={}
        for i in range(len(a)):
            if a[i] in da:
                da[a[i]]+=1
            else:
                da[a[i]]=1
                
            if b[i] in db:
                db[b[i]]+=1
            else:
                db[b[i]]=1
                
        for key,val in da.items():
            if db.get(key)!=val:
                return False
        return True
            
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        a,b=map(str,input().strip().split())
        if(Solution().isAnagram(a,b)):
            print("YES")
        else:
            print("NO") 
# } Driver Code Ends