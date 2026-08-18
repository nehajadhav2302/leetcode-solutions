from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q = deque([(beginWord, 1)])
        st = set(wordList)
        if beginWord in st:
            st.remove(beginWord)
        
        while q:
            word, step = q.popleft()

            if word == endWord:
                return step
            
            for i in range(len(word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    newWord = word[:i] + ch + word[i + 1:]

                    if newWord in st:
                        st.remove(newWord)
                        q.append((newWord, step + 1))
        return 0