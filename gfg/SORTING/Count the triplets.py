#User function Template for python3
class Solution:
	def countTriplet(self, arr, n):
		# code here
		
		#Using two pointer concept
		
		count=0
		arr.sort()
		
		for i in range(n-1,0,-1):
		    target=arr[i]
		    low=0
		    high=i-1
		    while(low<high):
		        curr=arr[low]+arr[high]
		        
		        if curr==target:
		            count+=1
		            low+=1
		            high-=1
		        elif curr>target:
		            high-=1
		        else:
		            low+=1
		return count
