
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
