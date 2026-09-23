class Solution:
    def reverseWords(self, s: str) -> str:
        s = reversed(list(s.split()))

        return " ".join(s)