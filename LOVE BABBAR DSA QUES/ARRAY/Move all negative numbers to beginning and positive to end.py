# 1st approach

def move(arr):
  arr.sort()
  
  
'''2nd approach- 
using 2 pointer concept '''



def shiftall(arr,left,right):
   
  # Loop to iterate while the
  # left pointer is less than
  # the right pointer
  while left<=right:
     
    # Condition to check if the left
    # and right pointer negative
    if arr[left] < 0 and arr[right] < 0:
      left+=1
       
    # Condition to check if the left
    # pointer element is positive and
    # the right pointer element is
    # negative
    else if arr[left]>0 and arr[right]<0:
      arr[left], arr[right] = \
              arr[right],arr[left]
      left+=1
      right-=1
       
    # Condition to check if the left
    # pointer is positive and right
    # pointer as well
    else if arr[left]>0 and arr[right]>0:
      right-=1
    else:
      left+=1
      right-=1
      
      
      
      '''
      3rd approach- 
       "Dutch National Flag Algorithm "
       The first color will be for all negative integers and the second color will be for all positive integers. We will divide the array into three partitions with the help of two pointers, low and high. 

ar[1…low-1] negative integers
ar[low…high] unknown
ar[high+1…N] positive integers
Now, we explore the array with the help of low pointer, shrinking the unknown partition, and moving elements to their correct partition in the process. We do this until we have explored all the elements, and size of the unknown partition shrinks to zero.

'''
      def reArrange(arr, n):
    low,high = 0, n - 1
    while(low<high):
        if(arr[low] < 0):
            low += 1
        elif(arr[high] > 0):
            high -= 1
        else:
            arr[low],arr[high] = arr[high],arr[low]
 
def displayArray(arr, n):
 
    for i in range(n):
        print(arr[i],end = " ")
   
    print('')
       
 
