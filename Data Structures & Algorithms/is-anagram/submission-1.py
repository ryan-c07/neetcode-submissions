class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = {}
        if len(s) != len(t):
            return False
        else:
            for i in range(len(s)):
                counts[s[i]] = counts.get(s[i], 0) + 1
                counts[t[i]] = counts.get(t[i], 0) - 1
            is_anagram = all(val == 0 for val in counts.values())
            return is_anagram
