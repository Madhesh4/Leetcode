class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Constants for 32-bit integer boundaries
        MAX_INT = 2147483647
        MIN_INT = -2147483648
        
        # Handle overflow case
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT
        
        # Determine if the result is negative
        negative = (dividend < 0) ^ (divisor < 0)
        
        # Work with absolute values
        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0
        
        # Binary search-like approach using bit shifts
        while dividend >= divisor:
            temp_divisor, count = divisor, 1
            # Double the divisor as much as possible
            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                count <<= 1
            
            # Subtract the largest found chunk and add to quotient
            dividend -= temp_divisor
            quotient += count
            
        return -quotient if negative else quotient