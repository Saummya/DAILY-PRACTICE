#Sort the array using insertion sort

class Solution:
    def insert(self, alist, index, n):
        #code here
        for i in range(1,len(alist)):
            key=alist[i]
            j=i-1
            while(j>=0 and key<alist[j]):
                alist[j+1]=alist[j]
                j-=1
            alist[j+1]=key
        return alist
        
        
        
        
    #Function to sort the list using insertion sort algorithm.    
    def insertionSort(self, alist, n):
        #code here
        
        self.insert(alist,i,n)

#{ 
#  Driver Code Starts
if __name__=="__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
    
        Solution().insertionSort(arr,n)
    
        for i in range(n):
            print(arr[i],end=" ")
    
        print()
# } Driver Code Ends