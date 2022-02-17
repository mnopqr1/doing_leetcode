from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:    
        c1 = Counter(word1)
        c2 = Counter(word2)
        
        letters1 = set(c1.keys())
        letters2 = set(c2.keys())
        
        profile1 = sorted(list(c1.values()))
        profile2 = sorted(list(c2.values()))
        
        return letters1 == letters2 and profile1 == profile2

