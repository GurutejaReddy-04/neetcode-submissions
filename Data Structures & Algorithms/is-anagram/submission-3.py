class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        S = [0] *26
        T = [0] *26
        for i in s:
            x = ord(i) - ord ('a') 
            S[x] += 1

        for i in t:
            x = ord(i) - ord ('a') 
            T[x] += 1
        
        if tuple(S) == tuple(T):
            return True
        else:
            return False