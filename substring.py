class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        # All words are the same length
        word_len = len(words[0]) 
        word_count = len(words)
        total_len = word_len * word_count
        target_map = Counter(words)
        results = []

        # We only need to check offsets from 0 to word_len - 1
        for i in range(word_len):
            left = i
            right = i
            current_map = Counter()
            count = 0
            
            while right + word_len <= len(s):
                # Extract the next word-sized block
                word = s[right : right + word_len]
                right += word_len
                
                if word in target_map:
                    current_map[word] += 1
                    count += 1
                    
                    # If we have too many of 'word', shrink from the left
                    while current_map[word] > target_map[word]:
                        left_word = s[left : left + word_len]
                        current_map[left_word] -= 1
                        count -= 1
                        left += word_len
                    
                    # If window size matches target, we found a match
                    if count == word_count:
                        results.append(left)
                else:
                    # Not a word in our list, reset the entire window
                    current_map.clear()
                    count = 0
                    left = right
                    
        return results
