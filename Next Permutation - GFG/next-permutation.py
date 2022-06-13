#User function Template for python3

class Solution:
    def nextPermutation(self, N, arr):
        # code here
    
        # 4,1,3,2
        # 0,1,2,3
        k=N-2
        while k >= 0:
            if arr[k] < arr[k + 1]:
                break
            k -= 1
            
        # reverse the list if the digit that is smaller than the
        # digit next to it is not found.
        if k < 0:
            arr = arr[::-1]
        else:
            
             # find the first greatest element than arr[k] from the 
                # end of the list
            for l in range(N - 1, k, -1):
                if arr[l] > arr[k]:
                    break
            # swap the elements at arr[k] and arr[l      
            arr[l], arr[k] = arr[k], arr[l]
            
            # reverse the list from k + 1 to the end to find the 
            # most nearest greater number to the given input number
            arr[k + 1:] = reversed(arr[k + 1:])
    
        return arr

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        ans = ob.nextPermutation(N, arr)
        for i in range(N):
            print(ans[i],end=" ")
        print()
# } Driver Code Ends