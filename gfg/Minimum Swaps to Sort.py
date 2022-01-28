'''
Medium Accuracy: 50.0% Submissions: 75734 Points: 4
Given an array of n distinct elements. Find the minimum number of swaps required to sort the array in strictly increasing order.


Example 1:

Input:
nums = {2, 8, 5, 4}
Output:
1
Explaination:
swap 8 with 4.
Example 2:

Input:
nums = {10, 19, 6, 3, 5}
Output:
2
Explaination:
swap 10 with 3 and swap 19 with 5.

Your Task:
You do not need to read input or print anything. Your task is to complete the function minSwaps() which takes the nums as input parameter and returns an integer denoting the minimum number of swaps required to sort the array. If the array is already sorted, return 0. 


Expected Time Complexity: O(nlogn)
Expected Auxiliary Space: O(n)


Constraints:
1 ≤ n ≤ 105
1 ≤ numsi ≤ 106
'''


class Solution:
    
    #Function to find the minimum number of swaps required to sort the array.
	def minSwaps(self, nums):
		#While iterating over the array, check the current element, 
		#and if not in the correct place, replace that element with 
		#the index of the element which should have come in this place.
		count=0
		temp=nums.copy()
		d={}     # Dictionary which stores the indexes of the input array
		temp.sort()
		n=len(nums)
		for i in range(n):
		    d[nums[i]]=i
		
		k=0
		for i in range(n):
		    if nums[i]!=temp[i]:
		        count+=1     #checking element is at right place or not
		        k=nums[i]
		        
		        
		        #if not on right place, swap with the index of the element which should come here
		        nums[i],nums[d[temp[i]]]=nums[d[temp[i]]], nums[i]
		        
		        #update the indexes in hashmap
		        d[k]=d[temp[i]]
		        d[temp[i]]=i
		return count
		        
		        
		        




#{ 
#  Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		obj = Solution()
		ans = obj.minSwaps(nums)
		print(ans)

# } Driver Code Ends
