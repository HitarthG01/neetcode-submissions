class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        clean_text = re.sub(r"[^a-zA-Z0-9]", "", s)
        clean_text=clean_text.lower()

        back=-1

        for count in range(0,len(clean_text)):
            
            if clean_text[count] != clean_text[back]:
                return False
            
            back=back-1
        
        return True
