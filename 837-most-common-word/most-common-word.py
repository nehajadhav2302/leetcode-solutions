class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        paragraph = paragraph.lower()
        banned = [word.lower() for word in banned]

        for ch in "!;,.'?":
            paragraph = paragraph.replace(ch, " ")
        
        words = paragraph.split()

        freq = {}
        for word in words:
            if word not in banned:
                freq[word] = freq.get(word, 0) + 1
        
        sorted_freq = sorted(freq.items(), key=lambda x:x[1], reverse = True)
        return sorted_freq[0][0]
