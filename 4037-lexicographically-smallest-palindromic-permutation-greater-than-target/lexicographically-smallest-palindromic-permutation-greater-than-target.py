from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        freq = Counter(s)
        
        # Check if a valid palindrome permutation exists
        odd_chars = [c for c, count in freq.items() if count % 2 != 0]
        if len(odd_chars) > 1:
            return ""
        
        mid_char = odd_chars[0] if odd_chars else ""
        
        # Available characters for the first half (length n // 2)
        half_freq = Counter()
        for c, count in freq.items():
            half_freq[c] = count // 2
        
        m = n // 2
        
        # Helper to build the palindrome given the first half
        def make_palindrome(first_half: str) -> str:
            second_half = first_half[::-1]
            return first_half + mid_char + second_half

        # Attempt to match prefix of length k with target[:k]
        target_half = target[:m]
        
        # Find the longest prefix match attempt from length m down to 0
        for k in range(m, -1, -1):
            # Check if target[:k] can be formed by available characters
            req = Counter(target_half[:k])
            if any(half_freq[c] < req[c] for c in req):
                continue
            
            # Remaining characters available after using target_half[:k]
            rem_freq = half_freq - req
            
            # Case 1: k == m (Exact match on first half)
            if k == m:
                first_half = target_half
                cand = make_palindrome(first_half)
                if cand > target:
                    return cand
                continue
            
            # Case 2: k < m, try to pick a character larger than target[k] at position k
            target_char = target[k]
            for next_char in sorted(rem_freq.keys()):
                if next_char > target_char and rem_freq[next_char] > 0:
                    # Pick next_char at index k
                    rem_freq[next_char] -= 1
                    
                    # Fill the rest of the first half lexicographically smallest
                    suffix_parts = []
                    for c in sorted(rem_freq.keys()):
                        suffix_parts.append(c * rem_freq[c])
                    
                    first_half = target_half[:k] + next_char + "".join(suffix_parts)
                    cand = make_palindrome(first_half)
                    if cand > target:
                        return cand
                    
                    rem_freq[next_char] += 1

        return ""