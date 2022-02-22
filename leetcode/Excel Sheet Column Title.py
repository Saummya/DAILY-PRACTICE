class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res=''
        while columnNumber>0:
            columnNumber-=1
            sec=columnNumber%26
            columnNumber=columnNumber//26
            
            res=chr(sec+ord('A'))+res
        
        return res
