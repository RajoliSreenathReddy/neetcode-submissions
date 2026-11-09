class Solution:
    def isPalindrome(self, s: str) -> bool:
        s.replace(" ","")
        res=[]
        for i in range(len(s)):
            if s[i].isalnum():
                res.append(s[i].lower())
        if ''.join(res)=="".join(res[::-1]):
            return True
        return False
        
