class Solution:
    def isValid(self, s: str) -> bool:
        l=[]
        d={'(':1,')':2,'[':3,']':4,'{':5,'}':6}
        for i in range(len(s)):
            if s[i] in '[{(':
                l.append(s[i])
                continue
            if l and d[l[-1]]-d[s[i]]==-1:
                l.pop()
            else:
                return False
        return True if not l else False