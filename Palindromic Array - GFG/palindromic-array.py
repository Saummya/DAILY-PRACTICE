# Your task is to complete this function
# Function should return True/False or 1/0
def PalinArray(arr ,n):
    # Code here
    ct=0
    for i in range(n):
        a1=arr[i]
        a2=[int(j) for j in str(a1)]
        
        if a2==a2[ : :-1]:
            ct+=1
    if ct==n:
        return True
    else:
        return False
        


#{ 
#  Driver Code Starts
# Driver Program
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        if PalinArray(arr, n):
            print(1)
        else:
            print(0)
# Contributed By: Harshit Sidhwa

# } Driver Code Ends