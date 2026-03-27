class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_ptr, p_ptr = 0, 0
        s_star, p_star = -1, -1
        
        while s_ptr < len(s):
            if p_ptr < len(p) and (p[p_ptr] == '?' or p[p_ptr] == s[s_ptr]):
                s_ptr += 1
                p_ptr += 1
            elif p_ptr < len(p) and p[p_ptr] == '*':
                p_star = p_ptr
                s_star = s_ptr
                p_ptr += 1
            elif p_star != -1:
                p_ptr = p_star + 1
                s_star += 1
                s_ptr = s_star
            else:
                return False
        
        while p_ptr < len(p) and p[p_ptr] == '*':
            p_ptr += 1
            
        return p_ptr == len(p)
