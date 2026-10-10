class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        paragraph = paragraph.lower()
        banned = [word.lower() for word in banned]
        banned = set(banned)
        
        for ch in "!;,.'?":
            paragraph = paragraph.replace(ch, " ")
        
        words = paragraph.split()

        freq = {}
        for word in words:
            if word not in banned:
                freq[word] = freq.get(word, 0) + 1
        
        max_count = 0
        freq_word = ""
        for key, value in freq.items():
            if value > max_count:
                max_count = value
                freq_word = key
        return freq_word
