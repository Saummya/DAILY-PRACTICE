class Solution:
    def toyCount(self, N, K, arr):
        # code here
        arr.sort()
        sum1=0
        count=0
        for i in range(N):
            sum1+=arr[i]
            if sum1<=K:
                count+=1
            else:
                break
        return count
