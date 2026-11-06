class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        mi=min(strs)
        l=[]
        for i in range(len(mi)):
            c=0
            for j in range(len(strs)):
                if strs[0][i]!=strs[j][i]:
                    break
                else:
                    c+=1
            if c==len(strs):
                l.append(strs[j][i])
            else:
                break
        return "".join(l)