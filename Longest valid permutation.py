class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]  # Base index for calculations
        max_length = 0
        
        for i, char in enumerate(s):
            if char == '(':
                # Always push the index of an opening bracket
                stack.append(i)
            else:
                # Pop the last opening bracket or base index
                stack.pop()
                
                if not stack:
                    # If empty, this ')' is a new base index
                    stack.append(i)
                else:
                    # Valid substring found: current index minus the new top
                    max_length = max(max_length, i - stack[-1])
        
        return max_length
