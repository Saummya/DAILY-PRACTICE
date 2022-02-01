'''
Given two strings S1 and S2 in lowercase, the task is to make them anagram. The only allowed operation is to remove a character from any string. Find the minimum number of characters to be deleted to make both the strings anagram. Two strings are called anagram of each other if one of them can be converted into another by rearranging its letters.

Example 1:

Input:
S1 = bcadeh
S2 = hea
Output: 3
Explanation: We need to remove b, c
and d from S1.
Example 2:

Input:
S1 = cddgk
S2 = gcd
Output: 2
Explanation: We need to remove d and
k from S1.
Your Task:
Complete the function remAnagram() which takes two strings S1, S2 as input parameter, and returns minimum characters needs to be deleted.

Expected Time Complexity: O(max(|S1|, |S2|)), where |S| = length of string S.
Expected Auxiliary Space: O(26)

Constraints:
1 <= |S1|, |S2| <= 105
'''
# function to calculate minimum numbers of characters
# to be removed to make two strings anagram
def remAnagram(str1,str2):
    
    #add code here
    '''c=0
    for ele in str1:
        if ele not in str2:
            c+=1
    return c
    '''
    
    count1 = [0]*26
    count2 = [0]*26
    i = 0
    while i < len(str1):
        count1[ord(str1[i])-ord('a')] += 1
        i += 1
    i =0
    while i < len(str2):
        count2[ord(str2[i])-ord('a')] += 1
        i += 1
    result = 0
    #count1.sort()
    #count2.sort()
    for i in range(26):
        result += abs(count1[i] - count2[i])
    return result
    
    
    

#{ 
#  Driver Code Starts
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        str1=input()
        str2=input()
        print(remAnagram(str1,str2))
# } Driver Code Ends
