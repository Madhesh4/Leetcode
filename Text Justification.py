class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        res = []
        line, line_len = [], 0
        
        for w in words:
            if line_len + len(w) + len(line) > maxWidth:
                for i in range(maxWidth - line_len):
                    line[i % (len(line) - 1 or 1)] += ' '
                res.append("".join(line))
                line, line_len = [], 0
            
            line.append(w)
            line_len += len(w)
            
        res.append(" ".join(line).ljust(maxWidth))
        return res
