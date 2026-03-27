class Solution:
    def isNumber(self, s: str) -> bool:
        digit = False
        dot = False
        exponent = False
        
        for i, char in enumerate(s):
            if char.isdigit():
                digit = True
            elif char in "+-":
                if i > 0 and s[i-1] not in "eE":
                    return False
            elif char in "eE":
                if exponent or not digit:
                    return False
                exponent = True
                digit = False
            elif char == ".":
                if dot or exponent:
                    return False
                dot = True
            else:
                return False
                
        return digit
