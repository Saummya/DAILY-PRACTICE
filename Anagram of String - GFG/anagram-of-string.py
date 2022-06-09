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