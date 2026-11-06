class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for i in strs:
            sr="".join(sorted(i))
            if sr in d:
                d[sr].append(i)
            else:
                d[sr]=[i]
        if d:
            l=[]
            for i in d:
                l.append(d[i])
            return l
        else:
            return [[""]]

