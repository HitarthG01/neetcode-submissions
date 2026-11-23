class Solution:
    def isValid(self, s: str) -> bool:

        brac_dict = {")": "(", "}": "{", "]": "["}
        stack = []

        for count in range(0, len(s)):
            if s[count] in "({[":
                stack.append(s[count])

            elif s[count] in ")}]":
                if stack != []:
                    if brac_dict[s[count]] == stack[(len(stack) - 1)]:
                        stack.pop()
                    elif brac_dict[s[count]] != stack[(len(stack) - 1)]:
                        return False
                elif stack == []:
                    return False
        if stack == []:   
            return True
        else:
            return False
