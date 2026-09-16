class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        answer = []

        for c in candies:
            if c + extraCandies >= max(candies):
                answer.append(True)
            else:
                answer.append(False)

        return answer