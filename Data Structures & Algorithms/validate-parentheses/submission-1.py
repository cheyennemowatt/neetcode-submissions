class Solution:
    def isValid(self, s: str) -> bool:
        #stack is only keeping track of open brackets
        stack = []

        pair = {')': '(' , ']':'[', '}':'{' }

        for char in s:
            #check if char is a open bracket
            if char not in pair:
                stack.append(char)
            else:
                #this means if we dont have a stack/ stack is empty
                #no stack with opens means nothing to check
                if not stack:
                    return False
                else: 
                    if stack.pop() != pair[char]:
                        return False
        #truly check if stack is empty
        return not stack
     

        