class Solution:
    def minStep(self, H, U, D):
        # code here
        '''
        sum1=U
        diff=0
        count=0
        while diff<=H:
            diff=sum1-D
            sum1+=diff
            count+=1
            
        return count+1
        '''
        
        count=0
        res=0
        while True:
            res+=U
            count+=1
            if res>H:
                break
            else:
                res-=D
       
        return count
