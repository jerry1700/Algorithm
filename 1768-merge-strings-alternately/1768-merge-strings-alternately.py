class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        answer = ""
        num = min(len(word1), len(word2))

        for i in range(num):
            answer += word1[i]
            answer += word2[i]

        answer += word1[num:]
        answer += word2[num:]

        return answer