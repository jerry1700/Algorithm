class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = []

        for i in s:
            if i in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                vowels.append(i)

        for idx, i in enumerate(s):
            if i in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                s = s[:idx] + vowels[-1] + s[idx + 1:] 
                vowels.pop()

        return s