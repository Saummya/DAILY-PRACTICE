class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        c=0
        res=0
        char1=chars
        
        for ele in words:
            c=0
            char1=chars
            
            for i in ele:
                if i in char1:
                    c+=1
                    char1=char1.replace(i," ",1)
                
            if c==len(ele):
                res+=len(ele)
        return res
