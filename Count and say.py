class Solution:
    def countAndSay(self, n: int) -> str:
        # Base case
        current_str = "1"
        
        # We need to find the nth term, so we run n-1 transformations
        for _ in range(n - 1):
            next_str = []
            i = 0
            
            # Run-length encoding of current_str
            while i < len(current_str):
                count = 1
                # Move forward while digits are the same
                while i + 1 < len(current_str) and current_str[i] == current_str[i+1]:
                    i += 1
                    count += 1
                
                # Append count + digit
                next_str.append(str(count))
                next_str.append(current_str[i])
                i += 1
            
            # Join the list to form the next string in the sequence
            current_str = "".join(next_str)
            
        return current_str
