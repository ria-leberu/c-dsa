class Solution:
    def isValid(self, s: str) -> bool:
        
        # dictionary to check parenthesis pairs 
        d = { "(":")", "{":"}", "[":"]"}

        stack = []

        for character in s:
            if character in d:
                stack.append(character)
            elif len(stack) == 0 or d[stack.pop()] != character:
                return False
        
        return len(stack) == 0
