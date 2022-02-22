class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        col=0
        for i in columnTitle:
            col=col*26+ ord(i)-ord('A')+1
        return col