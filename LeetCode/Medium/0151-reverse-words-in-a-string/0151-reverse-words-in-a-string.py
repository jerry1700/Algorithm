class Solution:
    def reverseWords(self, s: str) -> str:
        s = reversed(s.split())

        return " ".join(s)