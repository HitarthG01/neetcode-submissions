class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str1_dict={}
        str2_dict={}

        if len(s)!=len(t):
            return False

        else:
            for num in s:
                str1_dict[num]=str1_dict.get(num,0)+1

            for num in t:
                str2_dict[num]=str2_dict.get(num,0)+1

            return str1_dict==str2_dict