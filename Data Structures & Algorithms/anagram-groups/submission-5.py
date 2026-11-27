class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        sig_dict = {}

        for words in strs:
            sorted_word = "".join(sorted(words))
            sig_dict.setdefault(sorted_word, [])
            sig_dict[sorted_word].append(words)

        return list(sig_dict.values())
