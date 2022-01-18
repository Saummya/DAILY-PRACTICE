class Solution:
    def isGoodorBad(self, S):
        # code here 
        cons=0
        vowel=0
        n=len(S)
        for i in range(n):
            if (vowel>5 or cons>3):
                return 0
            if (S[i]=='a' or S[i]=='e' or S[i]=='i' or S[i]=='o' or S[i]=='u'):
                vowel+=1
                cons=0
            elif S[i]=='?':
                vowel+=1
                cons+=1
            else:
                cons+=1
                vowel=0
        return 1
