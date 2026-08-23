class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        mid = n // 2
        
        sum_diff = 0
        q_diff = 0
        
        for i in range(n):
            if i < mid:
                if num[i] == '?':
                    q_diff += 1
                else:
                    sum_diff += int(num[i])
            else:
                if num[i] == '?':
                    q_diff -= 1
                else:
                    sum_diff -= int(num[i])
        
        # Bob wins if and only if the difference in sum is 
        # perfectly offset by 9 for every 2 net '?' difference.
        return sum_diff * 2 != -q_diff * 9