# Your task is to complete this function
# Function should return True/False or 1/0
def PalinArray(arr ,n):
    # Code here
    count=0
    for i in range(n):
        x=arr[i]
        y=[int(j) for j in str(x)]
        
        if y==y[::-1]:
            count+=1
    if count==n:
        return 1
    else:
        return 0



#{ 
 # Driver Code Starts
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