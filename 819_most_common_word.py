from collections import Counter
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        result = []
        words = [word for word in re.sub('[^\w]', ' ', paragraph).lower().split()]
        for word in words:
            if word not in banned:
                result.append(word)

        counter_word = Counter(result)
        return counter_word.most_common(1)[0][0]