class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l=[]
        mx=word1 if len(word1)>len(word2) else word2
        mi=word1 if len(word1)<len(word2) else word2
        i=0
        while i<len(mx):
            if i<len(mi):
                l.append(word1[i])
                l.append(word2[i])
            else:
                l.append(mx[i])
            i+=1
        return "".join(l)
        
