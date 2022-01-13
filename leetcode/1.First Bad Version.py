class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''
        #APPROACH1-->LINEAR SEARCH-->T.C.=O(N)
        for i in range(n):
            if isBadVersion(i):
                return i
            
        return n          
        '''
         #APPROACH2-->BINARY SEARCH-->T.C.=O(log(N))
        start=0
        end=n-1
        
        while start<=end:
            mid=(start+end)//2
            if not isBadVersion(mid):
                start=mid+1
            else:
                end=mid-1
                
        return start
