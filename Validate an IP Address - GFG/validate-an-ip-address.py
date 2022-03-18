#User function Template for python3

def isValid(s):
    #code here
    a=s.split(".")
    l1=[]
    for i in range(0,256):
        l1.append(str(i))
    if len(a)==4:
        for i in a:
            if i not in l1:
                return 0
        return 1
    else:
        return 0


#{ 
#  Driver Code Starts
#Initial Template for Python 3

    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        if(isValid(s)):
            print(1)
        else:
            print(0)
    

# } Driver Code Ends