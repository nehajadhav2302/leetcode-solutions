class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        min_len = float('inf')
        ans = ""

        i = 0
        count_one = 0
        for j in range(len(s)):
            if s[j] == '1':
                count_one += 1
            
            while count_one == k:
                sub_len = j - i + 1
                sub_str = s[i: j+1]
                
                if sub_len < min_len:
                    min_len = sub_len
                    ans = sub_str
                elif sub_len == min_len:
                    ans = min(ans, sub_str)
                
                if s[i] == '1':
                    count_one -= 1
                i += 1
        return ans