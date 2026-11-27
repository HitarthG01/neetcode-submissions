class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dict_daddy = {}
        new_strs = []
        count = 0

        for words in strs:
            word = list(strs[count])
            word.sort()
            word = str(word)
            count = count + 1

            if word not in dict_daddy:
                dict_daddy[word] = []
                dict_daddy[word].append(words)

            elif word in dict_daddy:
                dict_daddy[word].append(words)

        for keys in dict_daddy.keys():
            new_strs.append(dict_daddy[keys])

        return new_strs
