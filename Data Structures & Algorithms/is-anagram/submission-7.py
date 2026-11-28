class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s)!=len(t) or (s=="" and t==""):
            return False
        else:
            dic_s={}
            dic_t={}
        
            for count in range(len(s)):

                dic_s.setdefault(s[count],0)
                dic_t.setdefault(t[count],0)
                dic_s[s[count]]=dic_s[s[count]]+1
                dic_t[t[count]]=dic_t[t[count]]+1
            
            return dic_s==dic_t


        