def maxSum(arr,n):
    # code here
    arr.sort()
    i=0
    j=n-1
    s=0
    while(i<j):
        s+=abs(arr[i]-arr[j])
        i+=1
        j-=1
    #s+=abs(arr[i]-arr[0])
    return s*2
    
    '''
    a[] = {4, 2, 1, 8}
    
    When I read this problem I just thought about it in the way that 
    every element will appear twice and there will be some elements that 
    will reduce from the sum and other who will contribute to the sum
    so think of it as target sum problem there will be one set that will reduce 
    the max sum and one set that will contribute to it.
    
 
    '''
